fun main() = with(System.`in`.bufferedReader()) {
    val N = readLine().toInt()
    val alphaMap = HashMap<Char, Boolean>()
    var result = 0
    
    repeat(N) {
        val word = readLine()
        var before: Char? = null
        var isGroup = true

        for (w in word) {
            if (before != null && before != w) {
                if (alphaMap.containsKey(w)){
                    isGroup = false
                    break
                }
            }
            
            alphaMap[before ?: w] = true
            before = w
        }
        if(isGroup)
            result += 1
    }
    
    print(result)
}