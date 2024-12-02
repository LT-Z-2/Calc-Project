; Currently configured for macOS
; remove _'s if you want it to be configured for windows (i think)

.text
.global _add
.global _subtract
.global _multiply
.global _divide

_add:
    fadd s0, s0, s1   // s0 = s0 + s1
    ret

_subtract:
    fsub s0, s0, s1   // s0 = s0 - s1
    ret

_multiply:
    fmul s0, s0, s1   // s0 = s0 * s1
    ret

_divide:
    fdiv s0, s0, s1   // s0 = s0 / s1
    ret