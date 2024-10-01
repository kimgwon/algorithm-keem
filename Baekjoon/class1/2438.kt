fun main() {
    val input = System.`in`.bufferedReader()
    val N = input.readLine().trimEnd().toInt()
    for (i in 1..N) {
        println("*".repeat(i))
    }
}