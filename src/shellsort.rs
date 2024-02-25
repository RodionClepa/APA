pub fn shell_sort(arr: &mut [f64], n: usize) -> usize{
    let mut gap: usize = n/2;
    
    while gap>0{
        for i in gap..n {
            let temp: f64 = arr[i];
            let mut j: usize=i;
            while j>=gap && arr[j-gap]>temp{
                arr[j] = arr[j-gap];
                j-=gap;
            }
            arr[j] = temp;
        }
        gap/=2;
    }
    return 0;
}