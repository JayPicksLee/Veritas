import { Button } from "@/components/ui/button";
import {
  Accordion,
  AccordionContent,
  AccordionItem,
  AccordionTrigger,
} from "@/components/ui/accordion";
import {
  Dialog,
  DialogClose,
  DialogContent,
  DialogDescription,
  DialogFooter,
  DialogHeader,
  DialogTitle,
  DialogTrigger,
} from "@/components/ui/dialog";
import { Input } from "@/components/ui/input";
import { Label } from "@/components/ui/label";
import { ModeToggle } from "@/components/mode-toggle";
import { Field, FieldDescription, FieldLabel } from "@/components/ui/field";
import {
  Card,
  CardAction,
  CardContent,
  CardDescription,
  CardFooter,
  CardHeader,
  CardTitle,
} from "@/components/ui/card";
import { Upload } from "lucide-react";
import { Dropzone } from "@/components/dropzone";

const items = [
  {
    value: "Functionality",
    trigger: "How does it work?",
    content:
      "We offer monthly and annual subscription plans. Billing is charged at the beginning of each cycle, and you can cancel anytime. All plans include automatic backups, 24/7 support, and unlimited team members.",
  },
  {
    value: "security",
    trigger: "Is my data secure?",
    content:
      "Yes. We use end-to-end encryption, SOC 2 Type II compliance, and regular third-party security audits. All data is encrypted at rest and in transit using industry-standard protocols.",
  },
  {
    value: "integration",
    trigger: "What integrations do you support?",
    content:
      "We integrate with 500+ popular tools including Slack, Zapier, Salesforce, HubSpot, and more. You can also build custom integrations using our REST API and webhooks.",
  },
];


export default function App() {
  return (
    <div className="p-8 min-h-screen flex flex-col">
      <header className="flex justify-end">
        <ModeToggle />
      </header>

      <main className="flex-1 mx-auto w-full max-w-3xl px-4 flex-col gap-16">
        <div className="flex-1 justify-center items-center flex flex-col min-h-[50vh] gap-4">
          <h1 className="text-3xl font-bold mb-4">AI Detector</h1>
          <br></br>
          <div className=" rounded-lg max-w-lg w-full mx-auto">
            <Dropzone />
          </div>
        </div>

        <section className="justify-center items-center flex flex-col gap-4">
          <Accordion
            type="single"
            collapsible
            className="max-w-lg rounded-lg border"
          >
            {items.map((item) => (
              <AccordionItem
                key={item.value}
                value={item.value}
                className="border-b px-4 last:border-b-0"
              >
                <AccordionTrigger>{item.trigger}</AccordionTrigger>
                <AccordionContent>{item.content}</AccordionContent>
              </AccordionItem>
            ))}
          </Accordion>
        </section>
      </main>

      
    </div>
  );
}
