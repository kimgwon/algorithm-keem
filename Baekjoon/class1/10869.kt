fun main() = with(System.`in`.bufferedReader()) {
    val (A, B) = readLine().split(" ").map{it.toInt()}
    println(A+B)
    println(A-B)
    println(A*B)
    println(A/B)
    println(A%B)
}