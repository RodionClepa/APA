fn merge(arr: &mut [f64], left: usize, mid: usize, right: usize){
    let sub_array_one_len: usize = mid-left+1;
    let sub_array_two_len: usize = right-mid;
    let mut left_array: Vec<f64> = vec![0.0; sub_array_one_len];
    let mut right_array: Vec<f64>  = vec![0.0; sub_array_two_len];

    for i in 0..sub_array_one_len{
        left_array[i] = arr[left+i];
    }
    for i in 0..sub_array_two_len{
        right_array[i] = arr[mid+1+i];
    }

    let mut index_of_sub_array_one = 0;
    let mut index_of_sub_array_two = 0;
    let mut index_of_merged_array = left;

    while index_of_sub_array_one<sub_array_one_len && index_of_sub_array_two<sub_array_two_len {
        if left_array[index_of_sub_array_one] <= right_array[index_of_sub_array_two] {
            arr[index_of_merged_array] = left_array[index_of_sub_array_one];
            index_of_sub_array_one+=1;
        }
        else{
            arr[index_of_merged_array] = right_array[index_of_sub_array_two];
            index_of_sub_array_two+=1;
        }
        index_of_merged_array+=1;
    }

    while index_of_sub_array_one<sub_array_one_len {
        arr[index_of_merged_array] = left_array[index_of_sub_array_one];
        index_of_merged_array+=1;
        index_of_sub_array_one+=1;
    }

    while index_of_sub_array_two<sub_array_two_len {
        arr[index_of_merged_array] = right_array[index_of_sub_array_two];
        index_of_merged_array+=1;
        index_of_sub_array_two+=1;
    }
}

pub fn merge_sort(arr: &mut [f64], begin: usize, end: usize){
    if begin>=end {
        return;
    }
    let mid: usize = begin+(end - begin)/2;
    merge_sort(arr, begin, mid);
    merge_sort(arr, mid+1, end);
    merge(arr, begin, mid, end);
}