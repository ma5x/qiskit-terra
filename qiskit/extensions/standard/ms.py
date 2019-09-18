# -*- coding: utf-8 -*-

# This code is part of Qiskit.
#
# (C) Copyright IBM 2017.
#
# This code is licensed under the Apache License, Version 2.0. You may
# obtain a copy of this license in the LICENSE.txt file in the root directory
# of this source tree or at http://www.apache.org/licenses/LICENSE-2.0.
#
# Any modifications or derivative works of this code must retain this
# copyright notice, and modified files need to carry a notice indicating
# that they have been altered from the originals.

# pylint: disable=invalid-name

"""
Molmer-Sorensen gate
"""

import numpy

from qiskit.circuit import Gate
from qiskit.circuit import QuantumCircuit
from qiskit.circuit import QuantumRegister
from qiskit.extensions.standard.cu1 import Cu1Gate
from qiskit.extensions.standard.h import HGate
from qiskit.extensions.standard.rx import RXGate
from qiskit.extensions.standard.ry import RYGate

class MSGate(Gate):
    """Molmer-Sorensen gate."""

    def __init__(self, theta):
        """Create new MS gate."""
        super().__init__("ms", 2, [theta])

    def _define(self):
        definition = []
        q = QuantumRegister(2, "q")
        rule = [
            (RYGate(numpy.pi/2), [q[0]], []),
            (HGate(), [q[1]], []),
            (Cu1Gate(2*self.params[0]), [q[0], q[1]], []),
            (HGate(), [q[1]], []),
            (RYGate(-numpy.pi/2), [q[0]], []),
            (RXGate(self.params[0]), [q[0]], []),
            (RXGate(-self.params[0]), [q[1]], [])
        ]
        for inst in rule:
            definition.append(inst)
        self.definition = definition

    def inverse(self):
        """Invert this gate."""
        return MSGate(-self.params[0])

def ms(self, theta,  q1, q2):
    """Apply MS to q1 and q2."""
    return self.append(MSGate(theta), [q1, q2], [])

QuantumCircuit.ms = ms
