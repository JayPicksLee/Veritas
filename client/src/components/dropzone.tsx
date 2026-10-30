import { Upload, CircleAlert } from "lucide-react";
import { useRef, useState } from "react";
import { cn } from "@/lib/utils";
import {Alert, AlertDescription, AlertTitle} from "@/components/ui/alert"
import {ACCEPTED_TYPES, MAX_SIZE_MB, validateFile} from "@/lib/validate"


export function Dropzone() {
  const [isDragging, setIsDragging] = useState(false);
  const [file, setFile] = useState<File | null>(null);
  const inputRef = useRef<HTMLInputElement>(null);
  const [error, setError] = useState<string | null>(null)

  function handleFile(selected: File | undefined) {
    if (!selected) return;
    console.log("we got here")
    const problem = validateFile(selected)
    console.log(problem)
    if (problem){
      setError(problem)
      setFile(null);
      return
    }

    console.log("file uploaded: ", selected);
    setError(null)
    setFile(selected)
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
        <Upload className="pointer-events-none size-8 text-muted-foreground" />
        <p className="pointer-events-none font-medium">
          Drop an image here, or click to browse
        </p>
        <p className="pointer-events-none text-sm text-muted-foreground">
          PNG, JPG or WebP, up to {MAX_SIZE_MB} MB
        </p>
        {file && <p className="pointer-events-none text-sm"></p>}
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
