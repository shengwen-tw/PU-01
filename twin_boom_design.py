###################################################################

wing_span = 1.13
wing_chord = 0.15
wing_area = wing_span *  wing_chord
wing_AR = (wing_span ** 2) / wing_area

wing_CL = 0.304
cruise_speed = 16.77
air_density = 1.225

takeoff_weight = (0.5 * wing_CL * air_density * (cruise_speed ** 2.0) * wing_area) / 9.8

###################################################################

TVCh = 0.6
Lh = 0.5
h_tail_AR = 4
h_tail_area = TVCh * wing_area * wing_chord / Lh
h_tail_span = (h_tail_area * h_tail_AR) ** 0.5
h_tail_chord = h_tail_area / h_tail_span

###################################################################

TVCv = 0.05
Lv = 0.5
v_tail_AR = 2
v_tail_area = TVCv * wing_area * wing_span / Lv
v_tail_area = v_tail_area / 2
#v_tail_span = (v_tail_area * v_tail_AR) ** 0.5
#v_tail_chord = v_tail_area / h_tail_span
v_tail_chord = h_tail_chord
v_tail_span = v_tail_area / v_tail_chord

###################################################################

#For rectangle wing only!
spar1_position = wing_span * 0.25
spar2_position = wing_span * 0.75
length_between_spar = wing_span * 0.5

###################################################################

print "__________________________________________________"

print "wing span = " + str(wing_span)
print "wing chord = " + str(wing_chord)
print "wing area = " + str(wing_area)
print "wing Aspect ratio= " + str(wing_AR)

print "__________________________________________________"

print "CL(0) = " + str(wing_CL) + " <--- 3D"
print "Cruise speed = " + str(cruise_speed) + "m/s"
print "air density = " + str(air_density)
print "Takeoff weight = " + str(takeoff_weight)

print "__________________________________________________"

print "Horizontal tail area: " + str(h_tail_area) + "m^2"
print "Horizontal tail span: " + str(h_tail_span * 100) + "cm"
print "Horizontal tail chord: " + str(h_tail_chord * 100) + "cm"

print "__________________________________________________"

print "Vertical tail area: " + str(v_tail_area) + "m^2 <--- Twin fin"
print "Vertical tail span: " + str(v_tail_span * 100) + "cm"
print "Vertical tail chord: " + str(v_tail_chord * 100) + "cm"

print "__________________________________________________"

print "Spar1 position = " + str(spar1_position)
print "Spar2 position = " + str(spar2_position)
print "Length between spars = " + str(length_between_spar)

print "__________________________________________________"

