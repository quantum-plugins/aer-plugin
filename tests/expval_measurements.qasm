OPENQASM 2.0;
include "qelib1.inc";

qreg q[2];
creg c[1];
measure q[0] -> c[0];
