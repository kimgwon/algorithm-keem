fun main() = with(System.`in`.bufferedReader()){
    val max_value = arrayOf(-1, -1)
    repeat(9) {
        val value = readLine().toInt()
        if (value > max_value[0]) {
            max_value[0] = value
            max_value[1] = it+1
        }
    }

    println(max_value[0])
    println(max_value[1])
}