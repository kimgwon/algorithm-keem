fun main() = with(System.`in`.bufferedReader()) {
    val n = readLine().toInt()
    var result = StringBuilder()
    repeat(n){
        val (r, p) = readLine().split(" ")
        p.forEach {
            result.append(it.toString().repeat(r.toInt()))
        }
        result.append("\n")
    }
    println(result)
}