export const ACCEPTED_TYPES = ["image/png", "image/jpg", "image/webp"]
export const MAX_SIZE_MB = 10
export const MAX_SIZE_BYTES = MAX_SIZE_MB  * 1024 * 1024

export function validateFile(file: File): string | null {
    if (!ACCEPTED_TYPES.includes(file.type)) {
        return "Wrong File Type. Select PNG, JPG, or WebP image."
    }
    if (file.size > MAX_SIZE_BYTES) {
        return `Image too large. Limit is ${MAX_SIZE_BYTES}`
    }
    return null
}