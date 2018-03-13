def posizione(x, y, v_x, v_y, dt):
    """Calcola la posizione di un corpo dopo un intervallo di tempo"""
    return x+(v_x*dt), y+(v_y*dt) 

def velocita (v_x, v_y, a_x, a_y, dt):
    """Calcola la velocità di un corpo"""
    return v_x+(a_x*dt), v_y+(a_y*dt)