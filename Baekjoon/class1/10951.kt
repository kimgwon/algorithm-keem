fun main() = with(System.`in`.bufferedReader()) {
    while (true) {
        val input = readLine()?.split(" ") ?: break
        if (input.size != 2) break
        val (A, B) = input.map{it.toInt()}
        println(A+B)
    }
}