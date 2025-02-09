OPENQASM 2.0;
include "qelib1.inc";

qreg q[4];
creg c[4];
measure q[0] -> c[0];
measure q[1] -> c[1];