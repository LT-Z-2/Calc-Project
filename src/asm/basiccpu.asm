; remove _'s if you want it to be configured for windows

section .text
    global _add
    global _subtract
    global _multiply
    global _divide

_add:
    mov eax, edi        ; Move first argument to EAX
    add eax, esi        ; Add second argument
    ret                 ; Return from function

_subtract:
    mov eax, edi        ; Move first argument to EAX
    sub eax, esi        ; Subtract second argument
    ret                 ; Return from function

_multiply:
    mov eax, edi        ; Move first argument to EAX
    imul eax, esi       ; Multiply by second argument
    ret                 ; Return from function

_divide:
    cmp esi, 0          ; Check if second argument is zero
    je div_by_zero       ; Jump to div_by_zero if it is zero
    mov eax, edi        ; Move first argument to EAX
    xor edx, edx        ; Clear EDX before division
    div esi             ; Divide EAX by ESI
    ret                 ; Return from function

div_by_zero:
    mov eax, -1         ; Return -1 for division by zero
    ret                 ; Return from function