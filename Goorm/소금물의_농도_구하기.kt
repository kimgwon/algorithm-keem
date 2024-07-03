import kotlin.math.*

fun main(args: Array<String>) = with(System.`in`.bufferedReader()) {
	val (N, M) = readLine().split(" ").map { it.toInt() }
	val result = (N * 0.07) / (N + M) * 100.0
	val formattedResult = floor(result * 100)/100
	println(String.format("%.2f", formattedResult))
}