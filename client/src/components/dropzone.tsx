import { Upload, CircleAlert, XIcon } from "lucide-react";
import { useRef, useState } from "react";
import { cn } from "@/lib/utils";
import {Alert, AlertDescription, AlertTitle} from "@/components/ui/alert"
import {ACCEPTED_TYPES, MAX_SIZE_MB, validateFile} from "@/lib/validate"
import {
  Attachment,
  AttachmentAction,
  AttachmentActions,
  AttachmentContent,
  AttachmentDescription,
  AttachmentMedia,
  AttachmentTitle,
} from "@/components/ui/attachment";
import { formatFileSize } from "@/lib/format";


export function Dropzone() {
  const [isDragging, setIsDragging] = useState(false);
  const [file, setFile] = useState<File | null>(null);
  const inputRef = useRef<HTMLInputElement>(null);
  const [error, setError] = useState<string | null>(null)
  const [previewUrl, setPreviewUrl] = useState<string | null>(null);

  function handleFile(selected: File | undefined) {
    if (!selected) return;

    if(previewUrl) URL.revokeObjectURL(previewUrl)

    const problem = validateFile(selected)

    console.log(problem)
    if (problem){
      setError(problem)
      setFile(null);
      setPreviewUrl(null)
      return
    }

    console.log("file uploaded: ", selected);
    setError(null)
    setFile(selected)
    setPreviewUrl(URL.createObjectURL(selected))
  }

  function handleDragOver(e: React.DragEvent<HTMLDivElement>) {
    e.preventDefault();
    setIsDragging(true);
  }

  function handleDragLeave() {
    setIsDragging(false);
  }

  function handleDrop(e: React.DragEvent<HTMLDivElement>) {
    e.preventDefault();
    setIsDragging(false);
    handleFile(e.dataTransfer.files[0]);
  }

  function handleChange(e: React.ChangeEvent<HTMLInputElement>) {
    handleFile(e.target.files?.[0]);
    e.target.value = "";
  }

  function handleRemove(e: React.MouseEvent) {
    e.stopPropagation();
    if (previewUrl) URL.revokeObjectURL(previewUrl);
    setPreviewUrl(null);
    setFile(null);
    setError(null);
    if (inputRef.current) inputRef.current.value = "";
  }

  return (
    <div className="mx-auto w-full max-w-xl space-y-4">
      <div
        className={cn(
          "cursor-pointer hover:bg-muted/50 transition-all duration-300 flex flex-col items-center justify-center gap-2 rounded-lg border-2 border-dashed border-border p-10 text-center transition-colors",
          isDragging && "border-primary bg-muted/50",
        )}
        onDragOver={handleDragOver}
        onDragLeave={handleDragLeave}
        onDrop={handleDrop}
        onClick={() => inputRef.current?.click()}
      >
        <input
          ref={inputRef}
          type="file"
          accept={ACCEPTED_TYPES.join(",")}
          className="hidden"
          onChange={handleChange}
        />

        {previewUrl && file ? (
          <Attachment orientation="vertical">
            <AttachmentMedia variant="image">
              <img src={previewUrl} alt={`Preview of ${file.name}`} />
            </AttachmentMedia>
            <AttachmentContent>
              <AttachmentTitle>{file.name}</AttachmentTitle>
              <AttachmentDescription>
                File size: {formatFileSize(file.size)}
              </AttachmentDescription>
            </AttachmentContent>
            <AttachmentActions>
              <AttachmentAction
                aria-label={`Remove ${file.name}`}
                onClick={handleRemove}
              >
                <XIcon />
              </AttachmentAction>
            </AttachmentActions>
          </Attachment>
        ) : (
          <>
            <Upload className="pointer-events-none size-8 text-muted-foreground" />
            <p className="pointer-events-none font-medium">
              Drop an image here, or click to browse
            </p>
            <p className="pointer-events-none text-sm text-muted-foreground">
              PNG, JPG or WebP, up to {MAX_SIZE_MB} MB
            </p>
          </>
        )}
      </div>

      {error && (
        <Alert variant="destructive">
          <CircleAlert />
          <AlertTitle>Can't use that file</AlertTitle>
          <AlertDescription>{error}</AlertDescription>
        </Alert>
      )}
    </div>
  );
}
