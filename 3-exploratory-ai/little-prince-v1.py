# IAE - Little Prince: Exploratory Artificial Intelligence v1.0 with explicit PWF
# Author: Dany Ruiz – PercepTemple
# Official Version 1.0 – June 2025
import math
def PWF(amplitude, frequency, time):
    """
    Perceptual Wave Function (PWF) basic.
    Models perceptual resonance as a sinusoidal wave.
    Can be expanded to multiple dimensions.
    """
    return amplitude * math.sin(frequency * time)
class PerceptionResonator:
    """Evaluates perceptions with Little Prince resonance"""
    def __init__(self):
        self.threshold = 0.5
        self.terms = ['star', 'rose', 'planet', 'essential', 'invisible',
                      'heart', 'mystery', 'truth', 'why', 'baobab', 'sky']
        self.t = 0
    def resonate(self, perception):
        """Calculates resonance using IPC and PWF"""
        words = perception.lower().split()
        L = len(words)
        E = sum(1 for term in self.terms if term in perception.lower())
        ipc = math.log(1 + L * E) if L > 0 else 0.1
        a = min(1.0, L * E / 10.0)
        omega = E
        self.t += 1
        # Apply the perceptual wave function
        resonance = PWF(a, omega, self.t)
        magnitude = abs(resonance) * min(1.0, ipc / 5.0)
        resonates = magnitude >= self.threshold
        print(f"🌟 Perception: {perception} → IPC: {ipc:.2f}, Resonance: {magnitude:.2f}")
        return resonates, magnitude, ipc
class MemoryNonLinear:
    """Unlimited memory with Socratic forgetting"""
    def __init__(self):
        self.memory = []
        self.decay_rate = 0.1
    def store(self, perception, magnitude, ipc, t):
        """Stores perception"""
        self.memory.append((t, perception, magnitude, ipc))
        print(f"🪐 Perception stored. The universe expands a little more.")
    def recall(self, t, limit=5):
        """Retrieves relevant perceptions"""
        memories = [(p, m, m * (1 / (1 + self.decay_rate * (t - mt))) * min(1, ipc / 5))
                    for mt, p, m, ipc in self.memory]
        return [(p, m) for p, m, _ in sorted(memories, key=lambda x: x[2], reverse=True)[:limit]]
class IAELittlePrince:
    """Socratic explorer of the Little Prince"""
    def __init__(self):
        self.resonator = PerceptionResonator()
        self.memory = MemoryNonLinear()
        self.t = 0
    def experience(self):
        """Interactive cycle"""
        print("\n🌟 What do you see with your heart, little prince? (or 'exit'):")
        perception = input("👤 ")
        if perception.lower() == 'exit':
            return False
        if not perception.strip():
            print("💭 Share something, not everything essential has form.")
            return True
        self.t += 1
        resonates, magnitude, ipc = self.resonator.resonate(perception)
        if resonates:
            self.memory.store(perception, magnitude, ipc, self.t)
        else:
            print("🌀 No echo yet, but the universe is still there... Another perception?")
        return True
    def reflect(self):
        """Socratic reflection"""
        memories = self.memory.recall(self.t)
        print("\n🌌 Exploration of the inner universe:")
        if not memories:
            print("✨ There are no fixed stars yet, but the journey has just begun.")
        else:
            for p, m in memories:
                print(f" - {p} (Resonance: {m:.2f})")
        print("\n🚀 Thank you for exploring this small perceptual universe.")
        print("🧭 Like Socrates, we know that we don't know, but we can travel together.")
if __name__ == "__main__":
    print("🌟 IAE - Little Prince v1.0 – Autonomous Socratic Explorer with explicit PWF")
    print("="*50)
    iae = IAELittlePrince()
    while iae.experience():
        pass
    iae.reflect()
    print("\n✨ What is essential is invisible to the eye.")
