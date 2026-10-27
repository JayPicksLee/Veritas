# Veritas

AI-generated images and videos are everywhere, and they keep getting better, which makes it harder and harder to tell what's real. Veritas is a tool that helps people make that judgement. You upload an image, and Veritas looks for evidence that it may have been AI-generated or edited, then explains what it found and how confident it is.

## Who it's for

Veritas is built to be accessible to everyone, with no technical knowledge needed. It's especially useful for people who regularly need to judge whether an image can be trusted, such as:

- **Journalists** checking images before they publish
- **Teachers** helping students think critically about what they see online
- **Moderators** reviewing content on platforms and communities
- **Anyone** who has come across an image online and wants a second opinion

## What Veritas isn't

- **It can't prove an image is real or fake.** No tool can do that with certainty. Veritas reports evidence and how confident it is, and leaves the final judgement to you.

- **It's one piece of evidence, not a final answer.** Use its results alongside other checks, like finding the original source of an image.

- **It shouldn't be relied on alone for serious decisions,** such as legal matters, or accusing someone of faking an image.

- **It only handles images for now.** Videos aren't supported yet, and uploads are limited to JPEG, PNG and WebP files up to 10 MB.

## How to run it

*Coming soon.*

## To-do

**Upload and validation**
- [x] Upload endpoint for images
- [x] Accept JPEG, PNG and WebP only, checked against the file's real contents
- [x] Reject empty, oversized and unreadable files
- [x] Reject images with extreme dimensions
- [x] Automated tests for upload and validation

**Project setup**
- [ ] Write the "How to run it" guide
- [ ] Run tests automatically on GitHub

**API and data**
- [ ] Store uploads and results in a database

**Analysis**
- [ ] Detect signals from image metadata
- [ ] Detect signals from compression patterns
- [ ] Explain findings in plain language, with confidence levels

**Later**
- [ ] Deploy Veritas online
- [ ] Train and evaluate a machine learning model
- [ ] Support video