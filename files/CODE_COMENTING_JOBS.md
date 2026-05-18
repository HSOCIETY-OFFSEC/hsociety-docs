# Remaining Code Documentation Tasks

## Status
Completed:
- Tier 1 Documentation
- Tier 2 Documentation
- Tier 3 Documentation

Remaining:
- Tier 4 (Layouts)
- Tier 5 (Utilities)
- Minor Shared Components Review

---

# Tier 4: Layout Documentation

## Goal
Document layout composition, navigation flow, responsive behavior, and shared structural logic.

## Files Remaining

### Shared Layouts
- `src/shared/layouts/AdminLayout.tsx`
- `src/shared/layouts/StudentLayout.tsx`
- `src/shared/layouts/LandingLayout.tsx`
- `src/shared/layouts/PublicLayout.tsx`
- `src/shared/layouts/SnapPublicLayout.tsx`

## What To Comment

### Layout Responsibilities
Explain:
- purpose of the layout
- which routes/pages use it
- shared wrappers/providers
- layout hierarchy

Example:
```ts
// Main authenticated student layout with persistent sidebar and top navigation
