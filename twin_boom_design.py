###################################################################

wing_span = 1.13
wing_chord = 0.15
wing_area = wing_span *  wing_chord
wing_AR = (wing_span ** 2) / wing_area

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
#v_tail_span = (v_tail_area * v_tail_AR) ** 0.5
#v_tail_chord = v_tail_area / h_tail_span
v_tail_chord = h_tail_chord
v_tail_span = v_tail_area / v_tail_chord

###################################################################

print "wing span = " + str(wing_span)
print "wing chord = " + str(wing_chord)
print "wing area = " + str(wing_area)
print "wing Aspect ratio= " + str(wing_AR)

print "_______________________________________"

print "Horizontal tail area: " + str(h_tail_area)
print "Horizontal tail span: " + str(h_tail_span * 100) + "cm"
print "Horizontal tail chord: " + str(h_tail_chord * 100) + "cm"

print "_______________________________________"

print "Vertical tail area: " + str(v_tail_area)
print "Vertical tail span: " + str(v_tail_span * 100) + "cm"
print "Vertical tail chord: " + str(v_tail_chord * 100) + "cm"

