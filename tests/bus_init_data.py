import numpy as np
import sympy as smp  # NOQA
from dian.system import System
import logging

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

system = System()

system.bus.add_element_with_defaults(14)
system.pq.add_element_with_defaults(8)
system.line.add_element_with_defaults(18)
system.pv.add_element_with_defaults(1)
system.shunt.add_element_with_defaults(1)

system.pq.bus = np.array([0, 2, 4, 6, 8])
system.pv.bus = np.array([0])
system.shunt.bus = np.array([2])

# system.line.bus1 = np.arange(0, 18)
# system.line.bus2 = np.arange(1, 19)

system.line.bus1 = np.random.randint(0, 14, (18, ))
system.line.bus2 = np.random.randint(0, 14, (18, ))

system.bus.metadata_check()
system.pq.metadata_check()
system.line.metadata_check()
system.pv.metadata_check()
system.shunt.metadata_check()

system.bus.init_data()
system.pq.init_data()
system.line.init_data()
system.pv.init_data()
system.shunt.init_data()

system.bus.get_var_address()
system.pq.get_var_address()
system.line.get_var_address()
system.pv.get_var_address()
system.shunt.get_var_address()

system.pq.get_algeb_ext()
system.line.get_algeb_ext()
system.pv.get_algeb_ext()
system.shunt.get_algeb_ext()

system.bus.init_equation()
system.pq.init_equation()
system.line.init_equation()
system.pv.init_equation()
system.shunt.init_equation()

system.pq.compute_param_int()
system.line.compute_param_int()
system.pv.compute_param_int()
system.shunt.compute_param_int()

system.pq.compute_param_custom()
system.line.compute_param_custom()
system.pv.compute_param_custom()
system.shunt.compute_param_custom()

system.pq.compute_variable()
system.line.compute_variable()
system.pv.compute_variable()
system.shunt.compute_variable()

system.pq.make_gcall_int_symbolic()
system.line.make_gcall_int_symbolic()
system.pv.make_gcall_int_symbolic()
system.shunt.make_gcall_int_symbolic()

system.pq.make_gcall_ext_symbolic()
system.line.make_gcall_ext_symbolic()
system.pv.make_gcall_ext_symbolic()
system.shunt.make_gcall_ext_symbolic()

system.dae.initialize_xyfg_empty()
system.collect_algeb_int_equations()
system.collect_algeb_ext_equations()
