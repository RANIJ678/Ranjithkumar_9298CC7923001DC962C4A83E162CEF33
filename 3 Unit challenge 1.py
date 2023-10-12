def linear_search_product(product_list, target_product):
  indices = []

  for index, product in enumerate(product_list):
    if product == target_product:
      indices.append(index)
  return indices


if __name__ == "__main__":
  products = ["Apple", "Banana", "Orange", "Apple", "Mango", "Apple"]
  target = "Apple"
  result_indices = linear_search_product(products, target)

  if result_indices:
    print(
        f"The target product '{target}' was found at indices: {result_indices}"
    )
  else:
    print(f"The target product '{target}' was not found in the list.")