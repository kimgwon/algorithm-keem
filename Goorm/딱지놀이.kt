fun main(args: Array<String>) = with(System.`in`.bufferedReader()){
	val N = readLine().toInt()
	
	repeat(N) {
		val initA = readLine().split(" ").map {it.toInt()}
		val initB = readLine().split(" ").map {it.toInt()}
		
		val A = MutableList<Int> (4) {0}
		val B = MutableList<Int> (4) {0}
		
		for (shape in initA.subList(1, initA.size)) {
			A[shape-1] += 1
		}
		for (shape in initB.subList(1, initB.size)) {
			B[shape-1] += 1
		}
		
		var isSame = true
		for (shape in 3 downTo 0) {
			if (A[shape] > B[shape]) {
				println("A")
				isSame = false
				break
			} else if (B[shape] > A[shape]) {
				println("B")
				isSame = false
				break
			}
		} 
		
		if (isSame) {
			println("D")
		}
	}
	println()
}