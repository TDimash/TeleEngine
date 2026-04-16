import React, { useState } from 'react';
import { motion, AnimatePresence } from 'motion/react';
import { 
  Bot, 
  Cpu, 
  Layers, 
  Zap, 
  Shield, 
  Code, 
  Terminal, 
  BookOpen, 
  ChevronRight, 
  Github,
  MessageSquare,
  Key,
  Database,
  Workflow
} from 'lucide-react';

const FeatureCard = ({ icon: Icon, title, description }: { icon: any, title: string, description: string }) => (
  <motion.div 
    whileHover={{ y: -5 }}
    className="p-6 bg-white/5 border border-white/10 rounded-2xl backdrop-blur-sm hover:border-white/20 transition-colors"
  >
    <div className="w-12 h-12 bg-blue-500/20 rounded-xl flex items-center justify-center mb-4 text-blue-400">
      <Icon size={24} />
    </div>
    <h3 className="text-xl font-semibold mb-2 text-white">{title}</h3>
    <p className="text-gray-400 leading-relaxed">{description}</p>
  </motion.div>
);

const CodeBlock = ({ code, language }: { code: string, language: string }) => (
  <div className="relative group">
    <div className="absolute -inset-0.5 bg-gradient-to-r from-blue-500 to-purple-600 rounded-xl blur opacity-20 group-hover:opacity-40 transition duration-1000 group-hover:duration-200"></div>
    <pre className="relative p-6 bg-gray-900 rounded-xl overflow-x-auto border border-white/10 font-mono text-sm leading-relaxed">
      <code className="text-blue-300">{code}</code>
    </pre>
  </div>
);

export default function App() {
  const [activeTab, setActiveTab] = useState('overview');

  const exampleCode = `import asyncio
from teleengine.bot import Bot
from teleengine.dispatcher import Dispatcher
from teleengine.types import Message
from teleengine.filters.builtin import CommandFilter

bot = Bot(token="YOUR_TOKEN")
dp = Dispatcher(bot)

@dp.message(CommandFilter(["start"]))
async def cmd_start(message: Message, bot: Bot):
    await bot.send_message(
        chat_id=message.chat.id,
        text="Hello! I'm your async bot."
    )

asyncio.run(dp.start_polling())`;

  return (
    <div className="min-h-screen bg-[#0a0a0a] text-gray-200 font-sans selection:bg-blue-500/30">
      {/* Navigation */}
      <nav className="border-b border-white/5 bg-black/50 backdrop-blur-xl sticky top-0 z-50">
        <div className="max-w-7xl mx-auto px-6 h-16 flex items-center justify-between">
          <div className="flex items-center gap-2">
            <div className="w-8 h-8 bg-blue-600 rounded-lg flex items-center justify-center text-white">
              <Bot size={20} />
            </div>
            <span className="font-bold text-xl tracking-tight text-white">TeleEngine</span>
          </div>
          <div className="hidden md:flex items-center gap-8 text-sm font-medium">
            <a href="#features" className="hover:text-white transition-colors">Features</a>
            <a href="#docs" className="hover:text-white transition-colors">Docs</a>
            <a href="#examples" className="hover:text-white transition-colors">Examples</a>
            <button className="px-4 py-2 bg-white text-black rounded-full hover:bg-gray-200 transition-colors">
              Get Started
            </button>
          </div>
        </div>
      </nav>

      {/* Hero Section */}
      <header className="relative pt-24 pb-32 overflow-hidden">
        <div className="absolute top-0 left-1/2 -translate-x-1/2 w-full max-w-4xl h-96 bg-blue-600/20 blur-[120px] -z-10 rounded-full" />
        <div className="max-w-7xl mx-auto px-6 text-center">
          <motion.div
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ duration: 0.6 }}
          >
            <h1 className="text-5xl md:text-7xl font-bold mb-6 tracking-tight text-white">
              Modern Async <br />
              <span className="text-transparent bg-clip-text bg-gradient-to-r from-blue-400 to-purple-500">
                TeleEngine Framework
              </span>
            </h1>
            <p className="text-xl text-gray-400 max-w-2xl mx-auto mb-10 leading-relaxed">
              A production-ready Python library built for performance, type-safety, and developer happiness. 
              Fully asynchronous with a powerful FSM and middleware system.
            </p>
            <div className="flex flex-col sm:flex-row items-center justify-center gap-4">
              <button className="w-full sm:w-auto px-8 py-4 bg-blue-600 text-white rounded-full font-semibold hover:bg-blue-700 transition-all flex items-center justify-center gap-2 group">
                Install Now <ChevronRight size={20} className="group-hover:translate-x-1 transition-transform" />
              </button>
              <button className="w-full sm:w-auto px-8 py-4 bg-white/5 text-white rounded-full font-semibold hover:bg-white/10 transition-all border border-white/10 flex items-center justify-center gap-2">
                <Github size={20} /> View Source
              </button>
            </div>
          </motion.div>
        </div>
      </header>

      {/* Features Grid */}
      <section id="features" className="py-24 bg-black/30">
        <div className="max-w-7xl mx-auto px-6">
          <div className="mb-16">
            <h2 className="text-3xl font-bold text-white mb-4">Why TeleEngine?</h2>
            <p className="text-gray-400">Everything you need to build scalable bots.</p>
          </div>
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
            <FeatureCard 
              icon={Zap} 
              title="Async First" 
              description="Built on top of asyncio and aiohttp for maximum concurrency and performance."
            />
            <FeatureCard 
              icon={Shield} 
              title="Type Safe" 
              description="Full type hinting and Pydantic models for all Telegram API objects. Mypy compatible."
            />
            <FeatureCard 
              icon={Workflow} 
              title="FSM Support" 
              description="Advanced Finite State Machine with multiple storage backends like Redis and Memory."
            />
            <FeatureCard 
              icon={Layers} 
              title="Middleware" 
              description="Powerful middleware system for logging, rate limiting, and context injection."
            />
            <FeatureCard 
              icon={Cpu} 
              title="Rate Limiting" 
              description="Automatic handling of Telegram's rate limits with built-in retry logic."
            />
            <FeatureCard 
              icon={Terminal} 
              title="Clean API" 
              description="Intuitive decorator-based handler registration and modular routing system."
            />
          </div>
        </div>
      </section>

      {/* Code Showcase */}
      <section id="examples" className="py-24">
        <div className="max-w-7xl mx-auto px-6">
          <div className="grid grid-cols-1 lg:grid-cols-2 gap-16 items-center">
            <div>
              <h2 className="text-4xl font-bold text-white mb-6">Simple yet powerful</h2>
              <p className="text-lg text-gray-400 mb-8 leading-relaxed">
                Registering handlers is as easy as adding a decorator. 
                Use built-in filters or create your own to handle complex logic with ease.
              </p>
              <ul className="space-y-4">
                {[
                  { icon: MessageSquare, text: "Command & Text filtering" },
                  { icon: Key, text: "State-aware handlers" },
                  { icon: Database, text: "Persistent storage" }
                ].map((item, i) => (
                  <li key={i} className="flex items-center gap-3 text-gray-300">
                    <div className="text-blue-500"><item.icon size={20} /></div>
                    {item.text}
                  </li>
                ))}
              </ul>
            </div>
            <CodeBlock code={exampleCode} language="python" />
          </div>
        </div>
      </section>

      {/* Footer */}
      <footer className="border-t border-white/5 py-12 bg-black">
        <div className="max-w-7xl mx-auto px-6 flex flex-col md:flex-row justify-between items-center gap-8">
          <div className="flex items-center gap-2">
            <Bot size={24} className="text-blue-500" />
            <span className="font-bold text-lg text-white">TeleEngine</span>
          </div>
          <div className="text-gray-500 text-sm">
            © 2026 TeleEngine Team. Built for the future of Telegram bots.
          </div>
          <div className="flex gap-6">
            <Github size={20} className="hover:text-white cursor-pointer transition-colors" />
            <MessageSquare size={20} className="hover:text-white cursor-pointer transition-colors" />
          </div>
        </div>
      </footer>
    </div>
  );
}
