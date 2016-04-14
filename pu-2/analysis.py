###################################################################

description = "PU-2 conventional rc aircraft analysis"

wing_span = 1.13 #m
wing_chord = 0.135 #m
wing_area = wing_span *  wing_chord
wing_AR = (wing_span ** 2) / wing_area

incident_angle = 3 #degree

wing_CL = 0.5264
cruise_speed = 16.8 #m/s
air_density = 1.225

takeoff_weight = (0.5 * wing_CL * air_density * (cruise_speed ** 2.0) * wing_area) / 9.8

static_margin = 0.1
cg_to_ac_length = wing_chord * static_margin

###################################################################

TVCh = 0.6
h_tail_span = 0.55
h_tail_chord = 0.11
h_tail_area = h_tail_span * h_tail_chord
h_tail_AR = (h_tail_span * h_tail_span) / h_tail_area
Lh = (TVCh * wing_area * wing_chord) / h_tail_area

###################################################################

CL_max = 1.2147
takeoff_weight = 1.2
stall_speed = (2 * takeoff_weight * 9.81 * air_density * wing_area * CL_max) ** 0.5

###################################################################

TVCv = 0.05
v_tail_chord = 0.11
v_tail_span = 0.15
v_tail_area = v_tail_span * v_tail_chord
v_tail_AR = (v_tail_span ** 2) / v_tail_area
Lv = (TVCv * wing_area * wing_span) / v_tail_area

###################################################################

def ms_to_kph(ms):
    return ms * 3.6

###################################################################

print "\n" + description

print "__________________________________________________"

print "wing span = " + str(wing_span)
print "wing chord = " + str(wing_chord)
print "wing area = " + str(wing_area)
print "wing Aspect ratio= " + str(wing_AR)

print "__________________________________________________"

print "CL(" + str(incident_angle) + ") = " + str(wing_CL) + " <--- 3D"
print "Cruise speed = " + str(cruise_speed) + "m/s ---> " + str(ms_to_kph(cruise_speed)) + "km/hr"
print "air density = " + str(air_density)
print "Takeoff weight = " + str(takeoff_weight)
print "Stall speed = " + str(stall_speed) + "ms ---> " + str(ms_to_kph(stall_speed)) + "km/hr"

print "__________________________________________________"

print "Static margin = " + str(static_margin)
print "Length from C.G to wing A.C = " + str(cg_to_ac_length * 100) + "cm"

print "__________________________________________________"

print "Horizontal tail area: " + str(h_tail_area) + "m^2"
print "Horizontal tail span: " + str(h_tail_span * 100) + "cm"
print "Horizontal tail chord: " + str(h_tail_chord * 100) + "cm"
print "Horizontal tail AR: " + str(h_tail_AR)
print "Lh: " + str(Lh)

print "__________________________________________________"

print "Vertical tail area: " + str(v_tail_area) + "m^2"
print "Vertical tail span: " + str(v_tail_span * 100) + "cm"
print "Vertical tail chord: " + str(v_tail_chord * 100) + "cm"
print "Vertical tail AR: " + str(v_tail_AR)
print "Lv: " + str(Lv)

print "__________________________________________________"
