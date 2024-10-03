fun main() = with(System.`in`.bufferedReader()){
    val T = readLine().toInt()
    repeat(T) {
        val (A, B) = readLine().split(" ").map{it.toInt()}
        println(A+B)
    }
}