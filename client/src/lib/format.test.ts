import { describe, it, expect } from "vitest"
import { formatFileSize } from "./format"

describe("formatFileSize", () => {
  it("shows bytes for tiny files", () => {
    expect(formatFileSize(500)).toBe("500 B")
  })

  it("shows whole KB for medium files", () => {
    expect(formatFileSize(2048)).toBe("2.00 KB")
  })

  it("shows one decimal place for MB", () => {
    expect(formatFileSize(5 * 1024 * 1024)).toBe("5.00 MB")
  })
})