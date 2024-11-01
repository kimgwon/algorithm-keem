fun main() = with(System.`in`.bufferedReader()) {
    val N = readLine().trim().toInt()
    val scores = readLine().split(" ").map { it.toDouble() }
    val max_score = scores.maxOrNull() ?: 1.0
    var sum_score = 0.0

    for (i in 0 until N) {
        sum_score += scores[i] / max_score * 100
    }

    print(sum_score / N)
}