class Solution:
    def flipAndInvertImage(self, image: list[list[int]]) -> list[list[int]]:
        for idx, tmp_img in enumerate(image):
            tmp_img.reverse()
            for tmp_idx, tmp_val in enumerate(tmp_img):
                if tmp_val == 1:
                    tmp_img[tmp_idx] = 0
                else:
                    tmp_img[tmp_idx] = 1
            image[idx] = tmp_img
        return image