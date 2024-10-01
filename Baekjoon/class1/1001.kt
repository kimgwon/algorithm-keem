fun main() = with(System.`in`.bufferedReader()) {
    val (A, B) = readLine().trimEnd().split(" ").map{ it.toInt() }
    print("${A-B}")
}