--- test.py	(original)
+++ test.py	(refactored)
@@ -42,20 +42,20 @@
 now = time.time()
 for seg1 in S:
 	if approx_equal(seg1[0][0], seg1[1][0], ev):
-		print 'VERTICAL SEG'
-		print ''
-		print ''
+		print('VERTICAL SEG')
+		print('')
+		print('')
 		vs = True
 	if approx_equal(seg1[0][1], seg1[1][1], ev):
-		print 'HORIZONTAL SEG'
-		print ''
-		print ''
+		print('HORIZONTAL SEG')
+		print('')
+		print('')
 		hs = True
 	for seg2 in S:
 		if seg1 is not seg2 and segs_equal(seg1, seg2):
-			print 'EQUAL SEGS'
-			print ''
-			print ''
+			print('EQUAL SEGS')
+			print('')
+			print('')
 			es = True
 		if seg1 is not seg2 and (seg2, seg1) not in seen:
 			i = intersect(seg1, seg2)
@@ -68,17 +68,17 @@
 				seen.append((seg1, seg2))
 later = time.time()
 n2time = later-now
-print "Line sweep results:"
+print("Line sweep results:")
 now = time.time()
 lsinters = intersection(S)
 inters = []
-for k, v in lsinters.iteritems():
+for k, v in lsinters.items():
 	#print '{0}: {1}'.format(k, v)
 	inters.append(k)
 #	inters.append(v)
 later = time.time()
-print 'TIME ELAPSED: {0}'.format(later-now)
-print "N^2 comparison results:"
+print('TIME ELAPSED: {0}'.format(later-now))
+print("N^2 comparison results:")
 pts_seen = []
 highestseen = 0
 for i in intersections:
@@ -97,14 +97,14 @@
 		if approx_equal(k[0], i[0][0], ev) and approx_equal(k[1], i[0][1], ev):
 			in_k = True
 	if in_k == False:
-		print 'Not in K: {0}: {1}'.format(i[0], i[1])
+		print('Not in K: {0}: {1}'.format(i[0], i[1]))
 #	print i
-print highestseen
-print 'TIME ELAPSED: {0}'.format(n2time)
+print(highestseen)
+print('TIME ELAPSED: {0}'.format(n2time))
 #print 'Missing from line sweep but in N^2:'
 #for i in seen:
 #	matched = False
-print len(lsinters)
-print len(pts_seen)
+print(len(lsinters))
+print(len(pts_seen))
 if len(lsinters) != len(pts_seen):
-	print 'uh oh!'
+	print('uh oh!')
