import numpy as np
import sympy as smp  # NOQA
from dian.system import System
import logging

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

system = System()

system.bus.n_elements_with_default_mapping(5)
system.pq.n_elements_with_default_mapping(3)
system.line.n_elements_with_default_mapping(6)
system.pv.n_elements_with_default_mapping(4)
system.shunt.n_elements_with_default_mapping(0)

system.pq.bus = np.array([1, 2, 3])
system.pv.bus = np.array([0, 1, 2, 4])
# system.shunt.bus = np.array([2])

system.line.bus1 = np.array([0, 0, 0, 1, 2, 3])
system.line.bus2 = np.array([1, 3, 4, 2, 3, 4])

system.bus.metadata_check()
system.pq.metadata_check()
system.line.metadata_check()
system.pv.metadata_check()
# system.shunt.metadata_check()

system.bus._init_data()
system.pq._init_data()
system.line._init_data()
system.pv._init_data()
# system.shunt._init_data()

system.bus.get_var_address()
system.pq.get_var_address()
system.line.get_var_address()
system.pv.get_var_address()
# system.shunt.get_var_address()

system.bus.get_algeb_ext()
system.pq.get_algeb_ext()
system.line.get_algeb_ext()
system.pv.get_algeb_ext()
# system.shunt.get_algeb_ext()

system.bus._init_equation()
system.pq._init_equation()
system.line._init_equation()
system.pv._init_equation()
# system.shunt._init_equation()

system.bus._compute_param_int()
system.pq._compute_param_int()
system.line._compute_param_int()
system.pv._compute_param_int()
# system.shunt._compute_param_int()

system.bus._compute_param_custom()
system.pq._compute_param_custom()
system.line._compute_param_custom()
system.pv._compute_param_custom()
# system.shunt._compute_param_custom()

system.bus._compute_variable()
system.pq._compute_variable()
system.line._compute_variable()
system.pv._compute_variable()
# system.shunt._compute_variable()

system.bus.make_gcall_int_symbolic()
system.pq.make_gcall_int_symbolic()
system.line.make_gcall_int_symbolic()
system.pv.make_gcall_int_symbolic()
# system.shunt.make_gcall_int_symbolic()

system.bus.make_gcall_ext_symbolic()
system.pq.make_gcall_ext_symbolic()
system.line.make_gcall_ext_symbolic()
system.pv.make_gcall_ext_symbolic()
# system.shunt.make_gcall_ext_symbolic()

system.dae.initialize_xyfg_empty()
system.collect_algeb_int_equations()
system.collect_algeb_ext_equations()
