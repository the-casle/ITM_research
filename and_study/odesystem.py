#!/usr/bin/env python
"""
A template file to simulate a specific system of Ordinary Differential Equations (ODEs).

... or an autogenerated script from the *crnsimulator* Python package.

Note: If this file is executable, it is *autogenerated*.
    This means it contains a system of hardcoded ODEs together with some
    default parameters. While it may be tempting to tweak some functions,
    beware that this file may be overwritten by the next execution of the
    `crnsimulator` executable.  Edits should be done at the source file:
    "crnsimulator.odelib_template.py" or you can provide an alternative
    template file. Use the option --output to avoid overwriting this file.

Usage: 
    python odesystem.py --help
"""

import logging
logger = logging.getLogger(__name__)

import argparse
import numpy as np
from scipy.integrate import odeint

class ODETemplateError(Exception):
    pass

rates = {
    
}

def odesystem(p0, t0, r):
    cBackbone, cBackbone_cData0_1s_to_left_with_backbone, cBackbone_cData1_1s_to_right_with_backbone, cData0_1s, cData0_1s_cStrip_to_left_with_strip, cData0_1s_right_with_backbone_to_failure_match, cData0_1s_right_with_strip_to_success_match, cData1_1s, cData1_1s_cStrip_to_right_with_strip, cData1_1s_left_with_backbone_to_failure_match, cData1_1s_left_with_strip_to_success_match, cStrip, cStrip_failure_match_to_left_with_backbone_right_with_strip, cStrip_right_with_backbone_to_cBackbone_right_with_strip, failure_match, failure_match_left_with_strip_to_left_with_backbone_success_match, failure_match_right_with_strip_to_right_with_backbone_success_match, left_with_backbone, left_with_backbone_right_with_strip_to_cBackbone_success_match, left_with_strip, left_with_strip_right_with_backbone_to_cBackbone_success_match, right_with_backbone, right_with_strip, success_match = p0
    if not r : r = rates


    dcBackbonedt = -0.0063937*cBackbone*cData0_1s - 0.007077*cBackbone*cData1_1s + 2.1502*cStrip_right_with_backbone_to_cBackbone_right_with_strip + 2.2114*left_with_backbone_right_with_strip_to_cBackbone_success_match + 3.6013*left_with_strip_right_with_backbone_to_cBackbone_success_match
    dcBackbone_cData0_1s_to_left_with_backbonedt = 0.0063937*cBackbone*cData0_1s - 2704200.0*cBackbone_cData0_1s_to_left_with_backbone
    dcBackbone_cData1_1s_to_right_with_backbonedt = 0.007077*cBackbone*cData1_1s - 6409900.0*cBackbone_cData1_1s_to_right_with_backbone
    dcData0_1sdt = -0.0063937*cBackbone*cData0_1s - 0.01146*cData0_1s*cStrip - 0.010981*cData0_1s*right_with_backbone - 0.018388*cData0_1s*right_with_strip
    dcData0_1s_cStrip_to_left_with_stripdt = 0.01146*cData0_1s*cStrip - 9181900.0*cData0_1s_cStrip_to_left_with_strip
    dcData0_1s_right_with_backbone_to_failure_matchdt = 0.010981*cData0_1s*right_with_backbone - 4549300.0*cData0_1s_right_with_backbone_to_failure_match
    dcData0_1s_right_with_strip_to_success_matchdt = 0.018388*cData0_1s*right_with_strip - 5733200.0*cData0_1s_right_with_strip_to_success_match
    dcData1_1sdt = -0.007077*cBackbone*cData1_1s - 0.0078468*cData1_1s*cStrip - 0.010682*cData1_1s*left_with_backbone - 0.0090014*cData1_1s*left_with_strip
    dcData1_1s_cStrip_to_right_with_stripdt = 0.0078468*cData1_1s*cStrip - 10266000.0*cData1_1s_cStrip_to_right_with_strip
    dcData1_1s_left_with_backbone_to_failure_matchdt = 0.010682*cData1_1s*left_with_backbone - 9863800.0*cData1_1s_left_with_backbone_to_failure_match
    dcData1_1s_left_with_strip_to_success_matchdt = 0.0090014*cData1_1s*left_with_strip - 11356000.0*cData1_1s_left_with_strip_to_success_match
    dcStripdt = -0.01146*cData0_1s*cStrip - 0.0078468*cData1_1s*cStrip - 6.5687e-5*cStrip*failure_match - 0.00035608*cStrip*right_with_backbone
    dcStrip_failure_match_to_left_with_backbone_right_with_stripdt = 6.5687e-5*cStrip*failure_match - 2.743*cStrip_failure_match_to_left_with_backbone_right_with_strip
    dcStrip_right_with_backbone_to_cBackbone_right_with_stripdt = 0.00035608*cStrip*right_with_backbone - 2.1502*cStrip_right_with_backbone_to_cBackbone_right_with_strip
    dfailure_matchdt = 4549300.0*cData0_1s_right_with_backbone_to_failure_match + 9863800.0*cData1_1s_left_with_backbone_to_failure_match - 6.5687e-5*cStrip*failure_match - 0.0008781*failure_match*left_with_strip - 0.00034445*failure_match*right_with_strip
    dfailure_match_left_with_strip_to_left_with_backbone_success_matchdt = 0.0008781*failure_match*left_with_strip - 4.0249*failure_match_left_with_strip_to_left_with_backbone_success_match
    dfailure_match_right_with_strip_to_right_with_backbone_success_matchdt = 0.00034445*failure_match*right_with_strip - 2.1147*failure_match_right_with_strip_to_right_with_backbone_success_match
    dleft_with_backbonedt = 2704200.0*cBackbone_cData0_1s_to_left_with_backbone - 0.010682*cData1_1s*left_with_backbone + 2.743*cStrip_failure_match_to_left_with_backbone_right_with_strip + 4.0249*failure_match_left_with_strip_to_left_with_backbone_success_match - 0.00011664*left_with_backbone*right_with_strip
    dleft_with_backbone_right_with_strip_to_cBackbone_success_matchdt = 0.00011664*left_with_backbone*right_with_strip - 2.2114*left_with_backbone_right_with_strip_to_cBackbone_success_match
    dleft_with_stripdt = 9181900.0*cData0_1s_cStrip_to_left_with_strip - 0.0090014*cData1_1s*left_with_strip - 0.0008781*failure_match*left_with_strip - 0.00061975*left_with_strip*right_with_backbone
    dleft_with_strip_right_with_backbone_to_cBackbone_success_matchdt = 0.00061975*left_with_strip*right_with_backbone - 3.6013*left_with_strip_right_with_backbone_to_cBackbone_success_match
    dright_with_backbonedt = 6409900.0*cBackbone_cData1_1s_to_right_with_backbone - 0.010981*cData0_1s*right_with_backbone - 0.00035608*cStrip*right_with_backbone + 2.1147*failure_match_right_with_strip_to_right_with_backbone_success_match - 0.00061975*left_with_strip*right_with_backbone
    dright_with_stripdt = -0.018388*cData0_1s*right_with_strip + 10266000.0*cData1_1s_cStrip_to_right_with_strip + 2.743*cStrip_failure_match_to_left_with_backbone_right_with_strip + 2.1502*cStrip_right_with_backbone_to_cBackbone_right_with_strip - 0.00034445*failure_match*right_with_strip - 0.00011664*left_with_backbone*right_with_strip
    dsuccess_matchdt = 5733200.0*cData0_1s_right_with_strip_to_success_match + 11356000.0*cData1_1s_left_with_strip_to_success_match + 4.0249*failure_match_left_with_strip_to_left_with_backbone_success_match + 2.1147*failure_match_right_with_strip_to_right_with_backbone_success_match + 2.2114*left_with_backbone_right_with_strip_to_cBackbone_success_match + 3.6013*left_with_strip_right_with_backbone_to_cBackbone_success_match
    return np.array([dcBackbonedt, dcBackbone_cData0_1s_to_left_with_backbonedt, dcBackbone_cData1_1s_to_right_with_backbonedt, dcData0_1sdt, dcData0_1s_cStrip_to_left_with_stripdt, dcData0_1s_right_with_backbone_to_failure_matchdt, dcData0_1s_right_with_strip_to_success_matchdt, dcData1_1sdt, dcData1_1s_cStrip_to_right_with_stripdt, dcData1_1s_left_with_backbone_to_failure_matchdt, dcData1_1s_left_with_strip_to_success_matchdt, dcStripdt, dcStrip_failure_match_to_left_with_backbone_right_with_stripdt, dcStrip_right_with_backbone_to_cBackbone_right_with_stripdt, dfailure_matchdt, dfailure_match_left_with_strip_to_left_with_backbone_success_matchdt, dfailure_match_right_with_strip_to_right_with_backbone_success_matchdt, dleft_with_backbonedt, dleft_with_backbone_right_with_strip_to_cBackbone_success_matchdt, dleft_with_stripdt, dleft_with_strip_right_with_backbone_to_cBackbone_success_matchdt, dright_with_backbonedt, dright_with_stripdt, dsuccess_matchdt])

def jacobian(p0, t0, r):
    cBackbone, cBackbone_cData0_1s_to_left_with_backbone, cBackbone_cData1_1s_to_right_with_backbone, cData0_1s, cData0_1s_cStrip_to_left_with_strip, cData0_1s_right_with_backbone_to_failure_match, cData0_1s_right_with_strip_to_success_match, cData1_1s, cData1_1s_cStrip_to_right_with_strip, cData1_1s_left_with_backbone_to_failure_match, cData1_1s_left_with_strip_to_success_match, cStrip, cStrip_failure_match_to_left_with_backbone_right_with_strip, cStrip_right_with_backbone_to_cBackbone_right_with_strip, failure_match, failure_match_left_with_strip_to_left_with_backbone_success_match, failure_match_right_with_strip_to_right_with_backbone_success_match, left_with_backbone, left_with_backbone_right_with_strip_to_cBackbone_success_match, left_with_strip, left_with_strip_right_with_backbone_to_cBackbone_success_match, right_with_backbone, right_with_strip, success_match = p0
    if not r : r = rates


    J = [[[] for i in range(len(p0))] for j in range(len(p0))]
    J[0][0] = -0.0063937*cData0_1s - 0.007077*cData1_1s
    J[0][1] = 0
    J[0][2] = 0
    J[0][3] = -0.0063937*cBackbone
    J[0][4] = 0
    J[0][5] = 0
    J[0][6] = 0
    J[0][7] = -0.007077*cBackbone
    J[0][8] = 0
    J[0][9] = 0
    J[0][10] = 0
    J[0][11] = 0
    J[0][12] = 0
    J[0][13] = 2.15020000000000
    J[0][14] = 0
    J[0][15] = 0
    J[0][16] = 0
    J[0][17] = 0
    J[0][18] = 2.21140000000000
    J[0][19] = 0
    J[0][20] = 3.60130000000000
    J[0][21] = 0
    J[0][22] = 0
    J[0][23] = 0
    J[1][0] = 0.0063937*cData0_1s
    J[1][1] = -2704200.00000000
    J[1][2] = 0
    J[1][3] = 0.0063937*cBackbone
    J[1][4] = 0
    J[1][5] = 0
    J[1][6] = 0
    J[1][7] = 0
    J[1][8] = 0
    J[1][9] = 0
    J[1][10] = 0
    J[1][11] = 0
    J[1][12] = 0
    J[1][13] = 0
    J[1][14] = 0
    J[1][15] = 0
    J[1][16] = 0
    J[1][17] = 0
    J[1][18] = 0
    J[1][19] = 0
    J[1][20] = 0
    J[1][21] = 0
    J[1][22] = 0
    J[1][23] = 0
    J[2][0] = 0.007077*cData1_1s
    J[2][1] = 0
    J[2][2] = -6409900.00000000
    J[2][3] = 0
    J[2][4] = 0
    J[2][5] = 0
    J[2][6] = 0
    J[2][7] = 0.007077*cBackbone
    J[2][8] = 0
    J[2][9] = 0
    J[2][10] = 0
    J[2][11] = 0
    J[2][12] = 0
    J[2][13] = 0
    J[2][14] = 0
    J[2][15] = 0
    J[2][16] = 0
    J[2][17] = 0
    J[2][18] = 0
    J[2][19] = 0
    J[2][20] = 0
    J[2][21] = 0
    J[2][22] = 0
    J[2][23] = 0
    J[3][0] = -0.0063937*cData0_1s
    J[3][1] = 0
    J[3][2] = 0
    J[3][3] = -0.0063937*cBackbone - 0.01146*cStrip - 0.010981*right_with_backbone - 0.018388*right_with_strip
    J[3][4] = 0
    J[3][5] = 0
    J[3][6] = 0
    J[3][7] = 0
    J[3][8] = 0
    J[3][9] = 0
    J[3][10] = 0
    J[3][11] = -0.01146*cData0_1s
    J[3][12] = 0
    J[3][13] = 0
    J[3][14] = 0
    J[3][15] = 0
    J[3][16] = 0
    J[3][17] = 0
    J[3][18] = 0
    J[3][19] = 0
    J[3][20] = 0
    J[3][21] = -0.010981*cData0_1s
    J[3][22] = -0.018388*cData0_1s
    J[3][23] = 0
    J[4][0] = 0
    J[4][1] = 0
    J[4][2] = 0
    J[4][3] = 0.01146*cStrip
    J[4][4] = -9181900.00000000
    J[4][5] = 0
    J[4][6] = 0
    J[4][7] = 0
    J[4][8] = 0
    J[4][9] = 0
    J[4][10] = 0
    J[4][11] = 0.01146*cData0_1s
    J[4][12] = 0
    J[4][13] = 0
    J[4][14] = 0
    J[4][15] = 0
    J[4][16] = 0
    J[4][17] = 0
    J[4][18] = 0
    J[4][19] = 0
    J[4][20] = 0
    J[4][21] = 0
    J[4][22] = 0
    J[4][23] = 0
    J[5][0] = 0
    J[5][1] = 0
    J[5][2] = 0
    J[5][3] = 0.010981*right_with_backbone
    J[5][4] = 0
    J[5][5] = -4549300.00000000
    J[5][6] = 0
    J[5][7] = 0
    J[5][8] = 0
    J[5][9] = 0
    J[5][10] = 0
    J[5][11] = 0
    J[5][12] = 0
    J[5][13] = 0
    J[5][14] = 0
    J[5][15] = 0
    J[5][16] = 0
    J[5][17] = 0
    J[5][18] = 0
    J[5][19] = 0
    J[5][20] = 0
    J[5][21] = 0.010981*cData0_1s
    J[5][22] = 0
    J[5][23] = 0
    J[6][0] = 0
    J[6][1] = 0
    J[6][2] = 0
    J[6][3] = 0.018388*right_with_strip
    J[6][4] = 0
    J[6][5] = 0
    J[6][6] = -5733200.00000000
    J[6][7] = 0
    J[6][8] = 0
    J[6][9] = 0
    J[6][10] = 0
    J[6][11] = 0
    J[6][12] = 0
    J[6][13] = 0
    J[6][14] = 0
    J[6][15] = 0
    J[6][16] = 0
    J[6][17] = 0
    J[6][18] = 0
    J[6][19] = 0
    J[6][20] = 0
    J[6][21] = 0
    J[6][22] = 0.018388*cData0_1s
    J[6][23] = 0
    J[7][0] = -0.007077*cData1_1s
    J[7][1] = 0
    J[7][2] = 0
    J[7][3] = 0
    J[7][4] = 0
    J[7][5] = 0
    J[7][6] = 0
    J[7][7] = -0.007077*cBackbone - 0.0078468*cStrip - 0.010682*left_with_backbone - 0.0090014*left_with_strip
    J[7][8] = 0
    J[7][9] = 0
    J[7][10] = 0
    J[7][11] = -0.0078468*cData1_1s
    J[7][12] = 0
    J[7][13] = 0
    J[7][14] = 0
    J[7][15] = 0
    J[7][16] = 0
    J[7][17] = -0.010682*cData1_1s
    J[7][18] = 0
    J[7][19] = -0.0090014*cData1_1s
    J[7][20] = 0
    J[7][21] = 0
    J[7][22] = 0
    J[7][23] = 0
    J[8][0] = 0
    J[8][1] = 0
    J[8][2] = 0
    J[8][3] = 0
    J[8][4] = 0
    J[8][5] = 0
    J[8][6] = 0
    J[8][7] = 0.0078468*cStrip
    J[8][8] = -10266000.0000000
    J[8][9] = 0
    J[8][10] = 0
    J[8][11] = 0.0078468*cData1_1s
    J[8][12] = 0
    J[8][13] = 0
    J[8][14] = 0
    J[8][15] = 0
    J[8][16] = 0
    J[8][17] = 0
    J[8][18] = 0
    J[8][19] = 0
    J[8][20] = 0
    J[8][21] = 0
    J[8][22] = 0
    J[8][23] = 0
    J[9][0] = 0
    J[9][1] = 0
    J[9][2] = 0
    J[9][3] = 0
    J[9][4] = 0
    J[9][5] = 0
    J[9][6] = 0
    J[9][7] = 0.010682*left_with_backbone
    J[9][8] = 0
    J[9][9] = -9863800.00000000
    J[9][10] = 0
    J[9][11] = 0
    J[9][12] = 0
    J[9][13] = 0
    J[9][14] = 0
    J[9][15] = 0
    J[9][16] = 0
    J[9][17] = 0.010682*cData1_1s
    J[9][18] = 0
    J[9][19] = 0
    J[9][20] = 0
    J[9][21] = 0
    J[9][22] = 0
    J[9][23] = 0
    J[10][0] = 0
    J[10][1] = 0
    J[10][2] = 0
    J[10][3] = 0
    J[10][4] = 0
    J[10][5] = 0
    J[10][6] = 0
    J[10][7] = 0.0090014*left_with_strip
    J[10][8] = 0
    J[10][9] = 0
    J[10][10] = -11356000.0000000
    J[10][11] = 0
    J[10][12] = 0
    J[10][13] = 0
    J[10][14] = 0
    J[10][15] = 0
    J[10][16] = 0
    J[10][17] = 0
    J[10][18] = 0
    J[10][19] = 0.0090014*cData1_1s
    J[10][20] = 0
    J[10][21] = 0
    J[10][22] = 0
    J[10][23] = 0
    J[11][0] = 0
    J[11][1] = 0
    J[11][2] = 0
    J[11][3] = -0.01146*cStrip
    J[11][4] = 0
    J[11][5] = 0
    J[11][6] = 0
    J[11][7] = -0.0078468*cStrip
    J[11][8] = 0
    J[11][9] = 0
    J[11][10] = 0
    J[11][11] = -0.01146*cData0_1s - 0.0078468*cData1_1s - 6.5687e-5*failure_match - 0.00035608*right_with_backbone
    J[11][12] = 0
    J[11][13] = 0
    J[11][14] = -6.5687e-5*cStrip
    J[11][15] = 0
    J[11][16] = 0
    J[11][17] = 0
    J[11][18] = 0
    J[11][19] = 0
    J[11][20] = 0
    J[11][21] = -0.00035608*cStrip
    J[11][22] = 0
    J[11][23] = 0
    J[12][0] = 0
    J[12][1] = 0
    J[12][2] = 0
    J[12][3] = 0
    J[12][4] = 0
    J[12][5] = 0
    J[12][6] = 0
    J[12][7] = 0
    J[12][8] = 0
    J[12][9] = 0
    J[12][10] = 0
    J[12][11] = 6.5687e-5*failure_match
    J[12][12] = -2.74300000000000
    J[12][13] = 0
    J[12][14] = 6.5687e-5*cStrip
    J[12][15] = 0
    J[12][16] = 0
    J[12][17] = 0
    J[12][18] = 0
    J[12][19] = 0
    J[12][20] = 0
    J[12][21] = 0
    J[12][22] = 0
    J[12][23] = 0
    J[13][0] = 0
    J[13][1] = 0
    J[13][2] = 0
    J[13][3] = 0
    J[13][4] = 0
    J[13][5] = 0
    J[13][6] = 0
    J[13][7] = 0
    J[13][8] = 0
    J[13][9] = 0
    J[13][10] = 0
    J[13][11] = 0.00035608*right_with_backbone
    J[13][12] = 0
    J[13][13] = -2.15020000000000
    J[13][14] = 0
    J[13][15] = 0
    J[13][16] = 0
    J[13][17] = 0
    J[13][18] = 0
    J[13][19] = 0
    J[13][20] = 0
    J[13][21] = 0.00035608*cStrip
    J[13][22] = 0
    J[13][23] = 0
    J[14][0] = 0
    J[14][1] = 0
    J[14][2] = 0
    J[14][3] = 0
    J[14][4] = 0
    J[14][5] = 4549300.00000000
    J[14][6] = 0
    J[14][7] = 0
    J[14][8] = 0
    J[14][9] = 9863800.00000000
    J[14][10] = 0
    J[14][11] = -6.5687e-5*failure_match
    J[14][12] = 0
    J[14][13] = 0
    J[14][14] = -6.5687e-5*cStrip - 0.0008781*left_with_strip - 0.00034445*right_with_strip
    J[14][15] = 0
    J[14][16] = 0
    J[14][17] = 0
    J[14][18] = 0
    J[14][19] = -0.0008781*failure_match
    J[14][20] = 0
    J[14][21] = 0
    J[14][22] = -0.00034445*failure_match
    J[14][23] = 0
    J[15][0] = 0
    J[15][1] = 0
    J[15][2] = 0
    J[15][3] = 0
    J[15][4] = 0
    J[15][5] = 0
    J[15][6] = 0
    J[15][7] = 0
    J[15][8] = 0
    J[15][9] = 0
    J[15][10] = 0
    J[15][11] = 0
    J[15][12] = 0
    J[15][13] = 0
    J[15][14] = 0.0008781*left_with_strip
    J[15][15] = -4.02490000000000
    J[15][16] = 0
    J[15][17] = 0
    J[15][18] = 0
    J[15][19] = 0.0008781*failure_match
    J[15][20] = 0
    J[15][21] = 0
    J[15][22] = 0
    J[15][23] = 0
    J[16][0] = 0
    J[16][1] = 0
    J[16][2] = 0
    J[16][3] = 0
    J[16][4] = 0
    J[16][5] = 0
    J[16][6] = 0
    J[16][7] = 0
    J[16][8] = 0
    J[16][9] = 0
    J[16][10] = 0
    J[16][11] = 0
    J[16][12] = 0
    J[16][13] = 0
    J[16][14] = 0.00034445*right_with_strip
    J[16][15] = 0
    J[16][16] = -2.11470000000000
    J[16][17] = 0
    J[16][18] = 0
    J[16][19] = 0
    J[16][20] = 0
    J[16][21] = 0
    J[16][22] = 0.00034445*failure_match
    J[16][23] = 0
    J[17][0] = 0
    J[17][1] = 2704200.00000000
    J[17][2] = 0
    J[17][3] = 0
    J[17][4] = 0
    J[17][5] = 0
    J[17][6] = 0
    J[17][7] = -0.010682*left_with_backbone
    J[17][8] = 0
    J[17][9] = 0
    J[17][10] = 0
    J[17][11] = 0
    J[17][12] = 2.74300000000000
    J[17][13] = 0
    J[17][14] = 0
    J[17][15] = 4.02490000000000
    J[17][16] = 0
    J[17][17] = -0.010682*cData1_1s - 0.00011664*right_with_strip
    J[17][18] = 0
    J[17][19] = 0
    J[17][20] = 0
    J[17][21] = 0
    J[17][22] = -0.00011664*left_with_backbone
    J[17][23] = 0
    J[18][0] = 0
    J[18][1] = 0
    J[18][2] = 0
    J[18][3] = 0
    J[18][4] = 0
    J[18][5] = 0
    J[18][6] = 0
    J[18][7] = 0
    J[18][8] = 0
    J[18][9] = 0
    J[18][10] = 0
    J[18][11] = 0
    J[18][12] = 0
    J[18][13] = 0
    J[18][14] = 0
    J[18][15] = 0
    J[18][16] = 0
    J[18][17] = 0.00011664*right_with_strip
    J[18][18] = -2.21140000000000
    J[18][19] = 0
    J[18][20] = 0
    J[18][21] = 0
    J[18][22] = 0.00011664*left_with_backbone
    J[18][23] = 0
    J[19][0] = 0
    J[19][1] = 0
    J[19][2] = 0
    J[19][3] = 0
    J[19][4] = 9181900.00000000
    J[19][5] = 0
    J[19][6] = 0
    J[19][7] = -0.0090014*left_with_strip
    J[19][8] = 0
    J[19][9] = 0
    J[19][10] = 0
    J[19][11] = 0
    J[19][12] = 0
    J[19][13] = 0
    J[19][14] = -0.0008781*left_with_strip
    J[19][15] = 0
    J[19][16] = 0
    J[19][17] = 0
    J[19][18] = 0
    J[19][19] = -0.0090014*cData1_1s - 0.0008781*failure_match - 0.00061975*right_with_backbone
    J[19][20] = 0
    J[19][21] = -0.00061975*left_with_strip
    J[19][22] = 0
    J[19][23] = 0
    J[20][0] = 0
    J[20][1] = 0
    J[20][2] = 0
    J[20][3] = 0
    J[20][4] = 0
    J[20][5] = 0
    J[20][6] = 0
    J[20][7] = 0
    J[20][8] = 0
    J[20][9] = 0
    J[20][10] = 0
    J[20][11] = 0
    J[20][12] = 0
    J[20][13] = 0
    J[20][14] = 0
    J[20][15] = 0
    J[20][16] = 0
    J[20][17] = 0
    J[20][18] = 0
    J[20][19] = 0.00061975*right_with_backbone
    J[20][20] = -3.60130000000000
    J[20][21] = 0.00061975*left_with_strip
    J[20][22] = 0
    J[20][23] = 0
    J[21][0] = 0
    J[21][1] = 0
    J[21][2] = 6409900.00000000
    J[21][3] = -0.010981*right_with_backbone
    J[21][4] = 0
    J[21][5] = 0
    J[21][6] = 0
    J[21][7] = 0
    J[21][8] = 0
    J[21][9] = 0
    J[21][10] = 0
    J[21][11] = -0.00035608*right_with_backbone
    J[21][12] = 0
    J[21][13] = 0
    J[21][14] = 0
    J[21][15] = 0
    J[21][16] = 2.11470000000000
    J[21][17] = 0
    J[21][18] = 0
    J[21][19] = -0.00061975*right_with_backbone
    J[21][20] = 0
    J[21][21] = -0.010981*cData0_1s - 0.00035608*cStrip - 0.00061975*left_with_strip
    J[21][22] = 0
    J[21][23] = 0
    J[22][0] = 0
    J[22][1] = 0
    J[22][2] = 0
    J[22][3] = -0.018388*right_with_strip
    J[22][4] = 0
    J[22][5] = 0
    J[22][6] = 0
    J[22][7] = 0
    J[22][8] = 10266000.0000000
    J[22][9] = 0
    J[22][10] = 0
    J[22][11] = 0
    J[22][12] = 2.74300000000000
    J[22][13] = 2.15020000000000
    J[22][14] = -0.00034445*right_with_strip
    J[22][15] = 0
    J[22][16] = 0
    J[22][17] = -0.00011664*right_with_strip
    J[22][18] = 0
    J[22][19] = 0
    J[22][20] = 0
    J[22][21] = 0
    J[22][22] = -0.018388*cData0_1s - 0.00034445*failure_match - 0.00011664*left_with_backbone
    J[22][23] = 0
    J[23][0] = 0
    J[23][1] = 0
    J[23][2] = 0
    J[23][3] = 0
    J[23][4] = 0
    J[23][5] = 0
    J[23][6] = 5733200.00000000
    J[23][7] = 0
    J[23][8] = 0
    J[23][9] = 0
    J[23][10] = 11356000.0000000
    J[23][11] = 0
    J[23][12] = 0
    J[23][13] = 0
    J[23][14] = 0
    J[23][15] = 4.02490000000000
    J[23][16] = 2.11470000000000
    J[23][17] = 0
    J[23][18] = 2.21140000000000
    J[23][19] = 0
    J[23][20] = 3.60130000000000
    J[23][21] = 0
    J[23][22] = 0
    J[23][23] = 0
    return J


def add_integrator_args(parser):
    """ODE integration aruments."""
    solver = parser.add_argument_group('odeint parameters')
    plotter = parser.add_argument_group('plotting parameters')

    # required: simulation time and output settings
    solver.add_argument("--t0", type=float, default=0, metavar='<flt>',
            help="First time point of the time-course.")
    solver.add_argument("--t8", type=float, default=100, metavar='<flt>',
            help="End point of simulation time.")
    plotter.add_argument("--t-lin", type=int, default=500, metavar='<int>',
            help="Returns --t-lin evenly spaced numbers on a linear scale from --t0 to --t8.")
    plotter.add_argument("--t-log", type=int, default=None, metavar='<int>',
            help="Returns --t-log evenly spaced numbers on a logarithmic scale from --t0 to --t8.")

    # required: initial concentration vector
    solver.add_argument("--p0", nargs='+', metavar='<int/str>=<flt>',
            help="""Vector of initial species concentrations. 
            E.g. \"--p0 1=0.5 3=0.7\" stands for 1st species at a concentration of 0.5 
            and 3rd species at a concentration of 0.7. You may chose to address species
            directly by name, e.g.: --p0 C=0.5.""")
    # advanced: scipy.integrate.odeint parameters
    solver.add_argument("-a", "--atol", type=float, default=None, metavar='<flt>',
            help="Specify absolute tolerance for the solver.")
    solver.add_argument("-r", "--rtol", type=float, default=None, metavar='<flt>',
            help="Specify relative tolerance for the solver.")
    solver.add_argument("--mxstep", type=int, default=0, metavar='<int>',
            help="Maximum number of steps allowed for each integration point in t.")

    # optional: choose output formats
    plotter.add_argument("--list-labels", action='store_true',
            help="Print all species and exit.")
    plotter.add_argument("--labels", nargs='+', default=[], metavar='<str>+',
            help="""Specify the (order of) species which should appear in the pyplot legend, 
            as well as the order of species for nxy output format.""")
    plotter.add_argument("--labels-strict", action='store_true',
            help="""When using pyplot, only plot tracjectories corresponding to labels,
            when using nxy, only print the trajectories corresponding to labels.""")
 
    plotter.add_argument("--nxy", action='store_true',
            help="Print time course to STDOUT in nxy format.")
    plotter.add_argument("--header", action='store_true',
            help="Print header for trajectories.")

    plotter.add_argument("--pyplot", default='', metavar='<str>',
            help="Specify a filename to plot the ODE simulation.")
    plotter.add_argument("--pyplot-xlim", nargs=2, type=float, default=None, metavar='<flt>',
            help="Specify the limits of the x-axis.")
    plotter.add_argument("--pyplot-ylim", nargs=2, type=float, default=None, metavar='<flt>',
            help="Specify the limits of the y-axis.")
    plotter.add_argument("--pyplot-labels", nargs='+', default=[], metavar='<str>+',
            help=argparse.SUPPRESS)
    return

def flint(inp):
    return int(float(inp)) if float(inp) == int(float(inp)) else float(inp)

def set_logger(verbose, logfile):
    # ~~~~~~~~~~~~~
    # Logging Setup 
    # ~~~~~~~~~~~~~
    logger.setLevel(logging.DEBUG)
    handler = logging.FileHandler(logfile) if logfile else logging.StreamHandler()
    if verbose == 0:
        handler.setLevel(logging.WARNING)
    elif verbose == 1:
        handler.setLevel(logging.INFO)
    elif verbose == 2:
        handler.setLevel(logging.DEBUG)
    elif verbose >= 3:
        handler.setLevel(logging.NOTSET)
    formatter = logging.Formatter('%(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)


def integrate(args, setlogger = False):
    """Main interface to solve the ODE-system.

    Args:
      args (:obj:`argparse.ArgumentParser()`): An argparse object containing all of
        the arguments of :obj:`crnsimulator.add_integrator_args()`.

    Prints:
      - plot files
      - time-course

    Returns:
      Nothing
    """
    if setlogger:
        set_logger(args.verbose, args.logfile)

    if args.pyplot_labels:
        logger.warning('Deprecated argument: --pyplot_labels.')

    svars = ["cBackbone", "cBackbone_cData0_1s_to_left_with_backbone", "cBackbone_cData1_1s_to_right_with_backbone", "cData0_1s", "cData0_1s_cStrip_to_left_with_strip", "cData0_1s_right_with_backbone_to_failure_match", "cData0_1s_right_with_strip_to_success_match", "cData1_1s", "cData1_1s_cStrip_to_right_with_strip", "cData1_1s_left_with_backbone_to_failure_match", "cData1_1s_left_with_strip_to_success_match", "cStrip", "cStrip_failure_match_to_left_with_backbone_right_with_strip", "cStrip_right_with_backbone_to_cBackbone_right_with_strip", "failure_match", "failure_match_left_with_strip_to_left_with_backbone_success_match", "failure_match_right_with_strip_to_right_with_backbone_success_match", "left_with_backbone", "left_with_backbone_right_with_strip_to_cBackbone_success_match", "left_with_strip", "left_with_strip_right_with_backbone_to_cBackbone_success_match", "right_with_backbone", "right_with_strip", "success_match"]

    p0 = [0] * len(svars)
    
    const = None
    #<&>CONSTANT_SPECIES_INFO<&>#
    if args.p0:
        for term in args.p0:
            p, o = term.split('=')
            try:
                pi = svars.index(p)
            except ValueError as e:
                pi = int(p) - 1
            finally:
                p0[pi] = flint(o)
    else:
        msg = 'Specify a vector of initial concentrations: ' + \
                'e.g. --p0 1=0.1 2=0.005 3=1e-6 (see --help)'
        if sum(p0) == 0:
            logger.warning(msg)
            args.list_labels = True
        else:
            logger.info(msg)

    if args.list_labels:
        print('List of variables and initial concentrations:')
        for e, v in enumerate(svars, 1):
            if args.labels_strict and e > len(args.labels):
                break
            print(f'{e} {v} {p0[e-1]} {"constant" if const and const[e-1] else ""}')
        raise SystemExit('Initial concentrations can be overwritten by --p0 argument')

    if not args.nxy and not args.pyplot:
        logger.warning('Use --pyplot and/or --nxy to plot your results.')

    if not args.t8:
        raise ODETemplateError('Specify a valid end-time for the simulation: --t8 <flt>')

    if args.t_log:
        if args.t0 == 0:
            raise ODETemplateError('--t0 cannot be 0 when using log-scale!')
        time = np.logspace(np.log10(args.t0), np.log10(args.t8), num=args.t_log)
    elif args.t_lin:
        time = np.linspace(args.t0, args.t8, num=args.t_lin)
    else:
        raise ODETemplateError('Please specify either --t-lin or --t-log. (see --help)')

    # It would be nice if it is possible to read alternative rates from a file instead.
    # None triggers the default-rates that are hard-coded in the (this) library file.
    rates = None

    logger.info(f'Initial concentrations: {list(zip(svars, p0))}')
    # TODO: logging should report more info on parameters.

    ny = odeint(odesystem,
        np.array(p0), time, (rates, ), Dfun = jacobian,
        atol=args.atol, rtol=args.rtol, mxstep=args.mxstep).T

    # Output
    if args.nxy and args.labels_strict:
        end = len(args.labels)
        if args.header:
            print(' '.join(['{:15s}'.format(x) for x in ['time'] + svars[:end]]))
        for i in zip(time, *ny[:end]):
            print(' '.join(map("{:.9e}".format, i)))
    elif args.nxy:
        if args.header:
            print(' '.join(['{:15s}'.format(x) for x in ['time'] + svars]))
        for i in zip(time, *ny):
            print(' '.join(map("{:.9e}".format, i)))

    if args.pyplot:
        from crnsimulator.plotting import ode_plotter
        plotfile = ode_plotter(args.pyplot, time, ny, svars,
                               log=True if args.t_log else False,
                               labels=set(args.labels),
                               xlim = args.pyplot_xlim,
                               ylim = args.pyplot_ylim,
                               labels_strict = args.labels_strict)
        logger.info(f"Plotting successfull. Wrote plot to file: {plotfile}")

    return zip(time, *ny)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("-v", "--verbose", action='count', default = 0,
        help = "Print logging output. (-vv increases verbosity.)")
    parser.add_argument('--logfile', default = '', action = 'store', metavar = '<str>',
        help = """Redirect logging information to a file.""")
    add_integrator_args(parser)
    args = parser.parse_args()
    integrate(args, setlogger = True)

