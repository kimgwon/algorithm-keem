fun main() = with(System.`in`.bufferedReader()) {
    val n = readLine().toInt()
    val nums = readLine().split(" ").map {it.toInt()}
    println("${nums.minOrNull()} ${nums.maxOrNull()}")
}