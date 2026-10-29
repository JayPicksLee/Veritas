import { Upload } from "lucide-react";

export function Dropzone() {
  return (
    <div className="flex flex-col items-center justify-center gap-2 rounded-lg border-2 border-dashed border-border p-10 text-center">
      <Upload className="size-8 text-muted-foreground" />
      <p className="font-medium">Drop an image here, or click to browse</p>
      <p className="text-sm text-muted-foreground">
        PNG, JPG or WebP, up to 5 MB
      </p>
    </div>
  );
}
