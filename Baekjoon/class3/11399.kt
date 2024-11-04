fun main() = with(System.`in`.bufferedReader()) {
    val N = readLine().trim().toInt()
    val people = readLine().split(" ").map { it.toInt() }.toMutableList()
    people.sort()
    
    for (i in 1 until N) {
        people[i] += people[i-1]
    }

    println(people.sum())
}