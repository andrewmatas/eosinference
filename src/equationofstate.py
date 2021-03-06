"""This module collects the available EOS models and allows one to call the EOS
model with the string eosname.
"""

import eospiecewisepolytrope

# Supported EOS models
eos_models = {
    'piecewise_polytrope_gamma_params':eospiecewisepolytrope.EOS4ParameterPiecewisePolytropeGammaParams,
    'piecewise_polytrope_p_params':eospiecewisepolytrope.EOS4ParameterPiecewisePolytropePParams,
    'piecewise_polytrope_log_p_params':eospiecewisepolytrope.EOS4ParameterPiecewisePolytropeLogPParams
}

# Supported initializers for the emcee walkers
initializers = {
    'piecewise_polytrope_gamma_params':eospiecewisepolytrope.initialize_walker_piecewise_polytrope_gamma_params,
    'piecewise_polytrope_p_params':eospiecewisepolytrope.initialize_walker_piecewise_polytrope_p_params,
    'piecewise_polytrope_log_p_params':eospiecewisepolytrope.initialize_walker_piecewise_polytrope_log_p_params 
}

def choose_eos_model(eosname):
    """Get the class reference for an EOS model.
    """
    if eosname in eos_models.keys():
        return eos_models[eosname]
    else:
        raise ValueError('EOS model name not valid.')

def initialize_walker_eos_params(eosname):
    """Find an initial point for the EOS parameters for an emcee walker.
    """
    if eosname in initializers.keys():
        return initializers[eosname]()
    else:
        raise ValueError('EOS model name not valid.')
