"""
Helper functions for creating LaTeX-style plots in physics lab reports
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc
from scipy import stats
from scipy.optimize import curve_fit


def setup_latex_plots():
    """
    Configure matplotlib for LaTeX-style rendering.
    Call this at the beginning of your notebook.
    """
    rc("font", **{"family": "serif", "serif": ["Latin Modern Roman"]})
    rc("text", usetex=True)
    rc("text.latex", preamble=r"\usepackage{lmodern}\usepackage{amsmath}")


def create_figure(width=6, height=4.5):
    """
    Create a figure with standard dimensions.

    Parameters:
    -----------
    width : float
        Figure width in inches (default: 6)
    height : float
        Figure height in inches (default: 4.5)

    Returns:
    --------
    fig, ax : matplotlib figure and axes objects
    """
    fig, ax = plt.subplots(figsize=(width, height))
    return fig, ax


def plot_with_fit(
    x,
    y,
    yerr=None,
    xlabel="",
    ylabel="",
    fit_type="linear",
    show_equation=True,
    residuals=False,
    **kwargs,
):
    """
    Create a professional plot with data points and fitted curve.

    Parameters:
    -----------
    x, y : array-like
        Data to plot
    yerr : array-like, optional
        Error bars for y data
    xlabel, ylabel : str
        Axis labels (LaTeX formatting supported)
    fit_type : str
        Type of fit: 'linear', 'quadratic', 'exponential', 'power'
    show_equation : bool
        Whether to show fit equation in legend
    residuals : bool
        Whether to show residuals subplot

    Returns:
    --------
    fig : matplotlib figure object
    results : dict
        Dictionary containing fit parameters and statistics
    """
    setup_latex_plots()

    if residuals:
        fig, (ax1, ax2) = plt.subplots(
            2, 1, figsize=(6, 6), height_ratios=[3, 1], sharex=True
        )
    else:
        fig, ax1 = plt.subplots(figsize=(6, 4.5))
        ax2 = None

    # Plot data points
    ax1.errorbar(
        x,
        y,
        yerr=yerr,
        fmt="o",
        markersize=8,
        capsize=3,
        capthick=1.5,
        label="Experimental data",
        markerfacecolor="none",
        markeredgewidth=1.5,
        **kwargs,
    )

    # Perform fit
    x_fit = np.linspace(x.min(), x.max(), 200)

    if fit_type == "linear":
        coeffs = np.polyfit(x, y, 1, w=1 / yerr if yerr is not None else None)
        y_fit = np.poly1d(coeffs)(x_fit)
        y_pred = np.poly1d(coeffs)(x)

        if show_equation:
            label = f"Linear fit: $y = {coeffs[0]:.4g}x + {coeffs[1]:.4g}$"
        else:
            label = "Linear fit"

    elif fit_type == "quadratic":
        coeffs = np.polyfit(x, y, 2, w=1 / yerr if yerr is not None else None)
        y_fit = np.poly1d(coeffs)(x_fit)
        y_pred = np.poly1d(coeffs)(x)

        if show_equation:
            label = f"Quadratic fit: $y = {coeffs[0]:.4g}x^2 + {coeffs[1]:.4g}x + {coeffs[2]:.4g}$"
        else:
            label = "Quadratic fit"

    elif fit_type == "exponential":

        def exp_func(x, a, b, c):
            return a * np.exp(b * x) + c

        popt, _ = curve_fit(exp_func, x, y, sigma=yerr)
        y_fit = exp_func(x_fit, *popt)
        y_pred = exp_func(x, *popt)

        if show_equation:
            label = f"Exponential fit: $y = {popt[0]:.4g}e^{{{popt[1]:.4g}x}} + {popt[2]:.4g}$"
        else:
            label = "Exponential fit"

    elif fit_type == "power":
        # Fit in log space for better stability
        log_coeffs = np.polyfit(np.log(x), np.log(y), 1)
        a = np.exp(log_coeffs[1])
        b = log_coeffs[0]
        y_fit = a * x_fit**b
        y_pred = a * x**b

        if show_equation:
            label = f"Power fit: $y = {a:.4g}x^{{{b:.4g}}}$"
        else:
            label = "Power fit"

    # Plot fit
    ax1.plot(x_fit, y_fit, "-", linewidth=1.5, label=label)

    # Calculate R-squared
    residuals_vals = y - y_pred
    ss_res = np.sum(residuals_vals**2)
    ss_tot = np.sum((y - np.mean(y)) ** 2)
    r_squared = 1 - (ss_res / ss_tot)

    # Format plot
    ax1.set_xlabel(xlabel)
    ax1.set_ylabel(ylabel)
    ax1.legend(loc="best", frameon=True)
    ax1.grid(True, alpha=0.3, linestyle="--")
    ax1.tick_params(direction="in")

    # Add residuals subplot if requested
    if residuals and ax2 is not None:
        ax2.axhline(y=0, color="k", linestyle="-", linewidth=0.8)
        ax2.plot(
            x,
            residuals_vals,
            "o",
            markersize=6,
            markerfacecolor="none",
            markeredgewidth=1.5,
        )
        ax2.set_xlabel(xlabel)
        ax2.set_ylabel("Residuals")
        ax2.grid(True, alpha=0.3, linestyle="--")
        ax2.tick_params(direction="in")

    plt.tight_layout()

    # Return results
    results = {
        "coefficients": coeffs if fit_type in ["linear", "quadratic"] else popt,
        "r_squared": r_squared,
        "residuals": residuals_vals,
    }

    return fig, results


def format_uncertainty(value, uncertainty, significant_figures=2):
    """
    Format a value with uncertainty in proper notation.

    Parameters:
    -----------
    value : float
        Measured value
    uncertainty : float
        Uncertainty in the measurement
    significant_figures : int
        Number of significant figures for uncertainty

    Returns:
    --------
    str : Formatted string like "1.234 ± 0.056"
    """
    # Determine decimal places based on uncertainty
    if uncertainty > 0:
        decimal_places = -int(np.floor(np.log10(uncertainty))) + (
            significant_figures - 1
        )
        decimal_places = max(0, decimal_places)
    else:
        decimal_places = 2

    return f"{value:.{decimal_places}f} ± {uncertainty:.{decimal_places}f}"


def calculate_propagated_error(func, values, uncertainties):
    """
    Calculate propagated uncertainty using partial derivatives.

    Parameters:
    -----------
    func : callable
        Function to propagate error through
    values : dict
        Dictionary of variable names and their values
    uncertainties : dict
        Dictionary of variable names and their uncertainties

    Returns:
    --------
    float : Propagated uncertainty
    """
    # Small step for numerical derivative
    h = 1e-8

    error_squared = 0
    for var, val in values.items():
        if var in uncertainties:
            # Calculate partial derivative numerically
            values_plus = values.copy()
            values_plus[var] = val + h
            values_minus = values.copy()
            values_minus[var] = val - h

            partial = (func(**values_plus) - func(**values_minus)) / (2 * h)
            error_squared += (partial * uncertainties[var]) ** 2

    return np.sqrt(error_squared)
