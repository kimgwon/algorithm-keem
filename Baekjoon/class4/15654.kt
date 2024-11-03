fun main() = with(System.`in`.bufferedReader()) {
    val (N, M) = readLine().split(" ").map { it.toInt() }
    val nums = readLine().split(" ").map { it.toInt() }.sorted()
    permutation(nums, M)
}

fun <T> permutation(arr: List<T>, r: Int) {
    val visited = BooleanArray(arr.size)

    fun permute(p: List<T>) {
        if (p.size == r) {
            println(p.joinToString(" "))
            return
        }
        repeat(arr.size) { idx ->
            if (!visited[idx]) {
                visited[idx] = true
                permute(p + arr[idx])
                visited[idx] = false
            }
        }
    }

    permute(listOf())
}