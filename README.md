# pyUdK


This library provides Udwadia Kalaba constrained parameters and force quantities functionality for Python 3 out of the box. The usage is mostly based on numpy and sympy library.

## Installation

Just run

    pip install pyUdK

If you want to use YAML to store your translations, use

    pip install pyUdK[YAML]

## Usage
### Basic usage

The simplest, though not very useful usage would be

    import Udk
    Q = Udk.ideal_Constraint_force(m, q, A, b)
