fun main() = with(System.`in`.bufferedReader()) {
    val (A, B) = readLine().split(" ").map {it.toInt()}
    println(String.format("%.10f", A / B.toDouble()))
}