import kotlin.math.*

fun main(args: Array<String>) = with(System.`in`.bufferedReader()) {
	val T = readLine().toInt()
	repeat(T) {
		val (X, Y, N) = readLine().split(" ").map {it.toInt()}
		val temp = N - (abs(X) + abs(Y))
		if (temp >= 0 && temp % 2 == 0) {
			println("YES")
		} else {
			println("NO")
		}
	}
}