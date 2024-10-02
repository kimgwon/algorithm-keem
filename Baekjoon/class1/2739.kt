fun main() = with(System.`in`.bufferedReader()) {
    val N = readLine().toInt()
    repeat(9) { i ->
        println("${N} * ${i+1} = ${N*(i+1)}")
    }
}