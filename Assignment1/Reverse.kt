class Reverse{
    fun reverse(arr:MutableList<Int>){
        for (i in 0 until arr.size / 2 ){
            Collections.swap(arr,i,arr.size -1 - i )
        }
    }
}
