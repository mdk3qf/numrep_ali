import numpy as np
import matplotlib.pyplot as plt

def dexp_true(t):
    return np.exp(t)

def fd_exp(t, h):
    derivative = (np.exp(t+h) - np.exp(t))/h
    return derivative

def cd_exp(t, h):
    derivative = (np.exp(t + h/2) - np.exp(t - h/2)) / h
    return derivative

def ed_exp(t, h):
    derivative = (8*(np.exp(t+h/4)-np.exp(t-h/4)) - (np.exp(t+h/2)-np.exp(t-h/2)))/3/h
    return derivative

def rel_error(approx, true):
    return np.abs((approx - true)/true)


t_values = [0.1, 1, 100]

fig, axes = plt.subplots(2, 3, gridspec_kw={'height_ratios': [1.5, 2]}, figsize=(20, 10))

for i, t in enumerate(t_values): 
    true_val = dexp_true(t)
    h_values, fd_vals, cd_vals, ed_vals = [], [], [], []
    fd_errs, cd_errs, ed_errs = [], [], []
    
    h = 1.0
    
    for h in np.logspace(-16, 0.5, 150): # machine precision for a 64-bit float,
        h_values.append(h)
        fd_vals.append(fd_exp(t, h))
        cd_vals.append(cd_exp(t, h))
        ed_vals.append(ed_exp(t, h))
        
        fd_errs.append(rel_error(fd_exp(t, h), true_val))
        cd_errs.append(rel_error(cd_exp(t, h), true_val))
        ed_errs.append(rel_error(ed_exp(t, h), true_val))
        
        h = h/2
    
    h_values = np.array(h_values)
    fd_vals = np.array(fd_vals)
    cd_vals = np.array(cd_vals)
    ed_vals = np.array(ed_vals)
    
    fd_errs = np.array(fd_errs)
    cd_errs = np.array(cd_errs)
    ed_errs = np.array(ed_errs)
    

    # top row
    ax_top = axes[0, i]
    ax_top.xaxis.grid(True)
    ax_top.yaxis.grid(True)
    ax_top.axhline(0, color="black", lw=1, linestyle="-")
    ax_top.plot(h_values, fd_vals, '--', label='Forward')
    ax_top.plot(h_values, cd_vals, ':', label='Central')
    ax_top.plot(h_values, ed_vals, '-', label='Extrapolated')
    ax_top.set_xscale('log')
    #ax_top.set_xlabel('h', fontsize=15)
    ax_top.set_ylabel(f"$\\frac{{d}}{{dt}} \\exp(t={t})$", fontsize=13)
    ax_top.legend()
    
    # bottom row
    ax_bot = axes[1, i]
    ax_bot.xaxis.grid(True)
    ax_bot.yaxis.grid(True)
    ax_bot.plot(h_values, fd_errs, '--', label='Forward')
    ax_bot.plot(h_values, cd_errs, ':', label='Central')
    ax_bot.plot(h_values, ed_errs, '-', label='Extrapolated')
    ax_bot.set_xscale('log')
    ax_bot.set_yscale('log')
    ax_bot.set_xlabel('h', fontsize=15)
    ax_bot.set_ylabel(r'$\varepsilon_{rel}$', fontsize=20)
    ax_bot.legend()

plt.savefig("exp_plots.png", dpi=300)