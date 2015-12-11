wing_span = 1.13
wing_chord = 0.15
wing_area = wing_span *  wing_chord
#############################
TVCh = 0.6
Lh = 0.5
h_tail_AR = 4
h_tail_area = TVCh * wing_area * wing_chord / Lh
h_tail_span = (wing_area * h_tail_AR) ** 0.5
h_tail_chord = h_tail_area / h_tail_span
#############################

print "wing area = " + str(wing_area)

print "Horizontal Tail area: " + str(h_tail_area)
print "Horizontal Tail span: " + str(h_tail_span * 100) + "cm"
print "Horizontal tail chord: " + str(h_tail_chord * 100) + "cm"