class MinMax{
    //returns the mimimum and maximum value in a list as a pair (min_value, max_value)
    fun min_max(arr:List<Int>):Pair<Int,Int>{
        var min = arr[0]
        var max = arr[0]

        for (i in 1 until arr.size){
            if(min > arr[i]){ min = arr[i] }
            else if (max < arr[i]){max = arr[i]}
        }
        return Pair(min, max)
    }
}
