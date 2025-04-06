def correspond(mot, mot_a_trous):
    if len(mot) != len(mot_a_trous):
        return False
    
    for c_mot, c_trou in zip(mot, mot_a_trous):
        if c_mot != c_trou and c_trou != "*":
            return False
    
    return True

print(correspond('INFORMATIQUE', 'INFO*MA*IQUE'))
print(correspond('AUTOMATIQUE', 'INFO*MA*IQUE'))
print(correspond('STOP', 'S*'))
print(correspond('AUTO', '*UT*'))
