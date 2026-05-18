# HSOCIETY Backend Documentation

## Overview

HSOCIETY Backend is the central service layer powering the HSOCIETY ecosystem.

The backend manages:
- authentication
- student lifecycle systems
- dashboards
- CP token systems
- blockchain integration
- notifications
- bootcamp infrastructure
- analytics
- security controls

The architecture follows a modular domain-driven structure designed for scalability and separation of concerns.

Unlike most backend projects that evolve through panic and caffeine hallucinations, this one actually has structure.

---

# High-Level Architecture

```text
Client Applications
        ↓
API Layer (Routes)
        ↓
Controllers
        ↓
Services
        ↓
Models / Blockchain / External Services
        ↓
Database + Storage
```

---

# Root Structure

```bash
hsociety-backend
├── core
├── modules
├── middleware
├── shared
├── scripts
├── test
├── docs
├── app.js
└── index.js
```

---

# Application Entry

## `index.js`

Primary runtime entry point.

### Responsibilities
- initialize backend server
- load environment configuration
- bootstrap application

### Notes
This file should remain minimal and focused on startup orchestration.

---

## `app.js`

Express application configuration layer.

### Responsibilities
- configure middleware
- register routes
- apply security policies
- initialize shared systems

### Typical Responsibilities
- CORS setup
- cookie parsing
- JSON parsing
- route mounting
- error handling

### Architectural Role
Acts as the central composition layer of the backend.

---

# Core Infrastructure

# `core/`

Contains shared infrastructure used across all modules.

---

## Core Configuration

### `core/config/endpoints.config.js`

Central API endpoint configuration.

### Responsibilities
- endpoint constants
- route mappings
- service references

### Purpose
Prevents hardcoded endpoint duplication across services and integrations.

Because manually repeating URLs everywhere is how developers slowly descend into clipboard-based madness.

---

# Database Layer

## `core/database/index.js`

Database connection manager.

### Responsibilities
- initialize database connection
- handle connection retries
- expose database utilities

### Likely Responsibilities
- MongoDB connection
- environment-specific configuration
- connection lifecycle management

---

# Logging System

## `core/logging/logger.js`

Centralized logging engine.

### Responsibilities
- structured logs
- error reporting
- request tracing
- operational visibility

### Recommended Future Improvements
- log levels
- external monitoring
- audit streams
- distributed tracing

---

# Core Middleware

## `core/middleware/`

Shared middleware layer for authentication, validation, and security.

---

## `auth.middleware.js`

Authentication enforcement middleware.

### Responsibilities
- JWT validation
- protected route access
- user identity resolution

---

## `core.middleware.js`

Global application middleware.

### Responsibilities
- shared request handling
- common API behavior
- request preprocessing

---

## `rateLimit.auth.js`

Authentication-specific rate limiting.

### Purpose
Protects sensitive endpoints from:
- brute force attacks
- OTP abuse
- credential stuffing

Humanity invented the internet and immediately used it to automate bad decisions.

---

## `validate.auth.js`

Authentication request validation.

### Responsibilities
- validate auth payloads
- sanitize login/register requests
- reject malformed input

---

## `validate.request.js`

Generic request validation middleware.

### Responsibilities
- schema validation
- payload integrity checks
- request normalization

---

# Notifications System

## `core/notifications/emit.js`

Central notification dispatcher.

### Responsibilities
- event broadcasting
- notification triggers
- system-wide event emission

### Possible Uses
- student alerts
- admin updates
- token events
- security notifications

---

# Security Layer

## `core/security/`

Centralized backend security infrastructure.

---

## `cookies.js`

Cookie configuration and security policies.

### Responsibilities
- secure cookie handling
- session persistence
- SameSite policies

---

## `email.js`

Email security configuration.

### Responsibilities
- SMTP configuration
- secure transport setup
- email validation rules

---

## `jwt.js`

JWT token management utilities.

### Responsibilities
- token creation
- token verification
- expiration handling
- refresh logic

---

## `origins.js`

CORS origin management.

### Responsibilities
- allowed origins
- cross-origin policies
- environment-safe access rules

---

## `rateLimiter.js`

Global rate limiting system.

### Responsibilities
- API abuse prevention
- request throttling
- endpoint protection

---

## `security.js`

Central security policy configuration.

### Responsibilities
- helmet configuration
- HTTP protections
- request hardening

---

# Core Services

## `core/services/`

Infrastructure-level shared services.

---

## `chain.service.js`

Blockchain integration service.

### Responsibilities
- communicate with HSOCIETY Chain
- submit blockchain events
- retrieve chain data

### Integration Targets
- CP token operations
- ledger synchronization
- proof/event systems

---

## `cpToken.service.js`

CP token system integration layer.

### Responsibilities
- token balance management
- reward calculations
- transaction coordination

### Notes
Acts as the economic backbone of the ecosystem.

Because every platform eventually invents points.
Then those points become currency.
Then someone asks if they can trade them.

---

## `email.service.js`

Email delivery abstraction layer.

### Responsibilities
- transactional emails
- OTP delivery
- notifications
- system messaging

---

## `pdf.service.js`

PDF generation service.

### Responsibilities
- certificates
- reports
- downloadable documents

### Future Possibilities
- achievement certificates
- student reports
- wallet statements

---

# Module Architecture

# `modules/`

Feature-driven domain structure.

Each module encapsulates:
- routes
- controllers
- services
- models
- validators
- middleware

This is good architecture.
Protect it from future “quick fixes.”

---

# Auth Module

## `modules/auth/`

Authentication and identity management system.

---

## Controllers

### `auth.controller.js`

Handles authentication request flow.

### Responsibilities
- login
- registration
- logout
- refresh token flow
- OTP verification

---

## Models

### `User.js`

Primary user model.

### Likely Fields
- identity data
- roles
- security metadata
- enrollment state

---

### `RefreshToken.js`

Refresh token persistence model.

### Responsibilities
- session persistence
- token rotation
- revocation tracking

---

## Services

### `auth.service.js`

Core authentication business logic.

### Responsibilities
- password handling
- account creation
- credential verification

---

### `otp.service.js`

OTP generation and validation.

### Responsibilities
- temporary verification codes
- expiration handling
- retry limits

---

### `twofa.service.js`

Two-factor authentication logic.

### Responsibilities
- secondary verification
- secure account protection

---

# CP Module

## `modules/cp/`

CP token and economy system.

---

## `cp.controller.js`

Handles CP-related API requests.

### Responsibilities
- balance retrieval
- transaction operations
- token interactions

---

## `cp.routes.js`

CP token route definitions.

---

# Dashboards Module

## `modules/dashboards/`

Administrative analytics and dashboard systems.

---

## Models

### `CaseStudy.js`
Stores dashboard educational or analytical content.

---

### `DashboardActivity.js`
Tracks dashboard/system activity.

---

## Routes

### `admin.routes.js`
Administrative dashboard endpoints.

---

### `ctf.admin.routes.js`
CTF administration endpoints.

---

## Services

### `admin.service.js`

Administrative business logic layer.

### Responsibilities
- analytics aggregation
- admin workflows
- operational insights

---

# Learn Module

## `modules/learn/`

Educational rule and learning systems.

---

## `LearnRule.js`

Defines educational progression logic and learning rules.

---

# Notifications Module

## `modules/notifications/`

Notification storage and delivery infrastructure.

---

## `Notification.js`

Notification persistence model.

### Responsibilities
- notification tracking
- delivery state
- user targeting

---

## `notifications.routes.js`

Notification API endpoints.

---

# Shared Module

## `modules/shared/`

Cross-platform shared resources.

---

## Shared Models

### `ContactMessage.js`
Stores public contact submissions.

---

### `CPProduct.js`
Marketplace or token product representation.

---

### `CPTransaction.js`
Tracks CP token transactions.

---

### `SecurityEvent.js`
Security monitoring and audit events.

---

### `SiteContent.js`
Dynamic CMS-like platform content.

---

### `Subscription.js`
Subscription and membership management.

---

## Shared Routes

### `public.routes.js`
Public-facing API endpoints.

---

### `upload.routes.js`
File upload endpoints.

### Security Importance
Uploads should always enforce:
- file validation
- size limits
- MIME restrictions

Because the internet absolutely will upload malware disguised as a cat photo.

---

# Student Module

## `modules/student/`

Core educational platform engine.

This is one of the most important modules in the entire backend.

---

## Controllers

### `student.controller.js`

Student-focused request orchestration.

### Responsibilities
- progress tracking
- bootcamp access
- dashboard data
- learning state

---

## Middleware

### `student.middleware.js`

Student-specific authorization and access logic.

---

## Student Models

### Core Educational Models
- `StudentProfile.js`
- `StudentOverview.js`
- `StudentCourse.js`

### Bootcamp Systems
- `BootcampRoomSession.js`

### Quiz Systems
- `Quiz.js`
- `QuizSubmission.js`

### CTF Systems
- `CTFChallenge.js`
- `CTFSubmission.js`

---

# Student Routes

## `student.routes.js`

Primary student API layer.

---

## `profile.routes.js`

Profile management endpoints.

---

## `ctf.routes.js`

CTF interaction routes.

---

## `ctf.helpers.js`

Shared helper logic for CTF systems.

---

## `ctf.sandbox.js`

Sandbox execution/testing environment.

### Security Warning
Sandbox systems require careful isolation.

Never trust user-controlled execution environments.
Humans will weaponize calculators if given enough time.

---

# Student Services

## `student.lifecycle.service.js`

Student progression orchestration engine.

### Responsibilities
- onboarding
- enrollment state
- progression tracking
- lifecycle transitions

This file likely contains important business rules.

Document it heavily.

---

# Shared Infrastructure

# `shared/`

Cross-module shared utilities and configuration.

---

## `shared/config/bootcamp.config.js`

Bootcamp configuration system.

### Responsibilities
- bootcamp metadata
- progression settings
- ecosystem constants

---

## Shared Utils

### `overviewCache.js`

Dashboard overview caching system.

### Purpose
- reduce database load
- improve dashboard response time

---

### `engagementMetrics.js`

Student engagement analytics utilities.

### Responsibilities
- participation metrics
- activity scoring
- engagement calculations

---

# Scripts

# `scripts/`

Operational automation and migrations.

---

## Migrations

### Examples
- enrollment migrations
- access recovery
- balance restoration
- legacy cleanup

### Importance
Migration scripts preserve data consistency across evolving platform versions.

---

## `seed-quizzes.mjs`

Quiz data seeding utility.

### Responsibilities
- populate initial quiz content
- testing support
- onboarding datasets

---

# Testing

# `test/`

Backend validation and reliability tests.

---

## `health.test.mjs`

Backend health verification.

---

## `auto-bootcamp-enrollment/index.test.mjs`

Enrollment workflow testing.

### Purpose
Ensures automated lifecycle systems behave correctly.

---

# Documentation

# `docs/`

System architecture and integration references.

---

## Existing Docs
- `ARCHITECTURE.md`
- `auth-backend-plan.md`
- `CHAIN_INTEGRATION.md`
- `CP_TOKEN_READ_MODEL.md`
- `FRONTEND_CONTRACT.md`

These documents form the operational knowledge base of the backend.

Keep them synchronized with implementation changes.
Outdated documentation becomes historical fiction surprisingly fast.

---

# Recommended Commenting Priorities

## Highest Priority Files

1. `auth.service.js`
2. `student.lifecycle.service.js`
3. `chain.service.js`
4. `cpToken.service.js`
5. `auth.middleware.js`
6. `validate.request.js`
7. `admin.service.js`
8. `student.controller.js`
9. `ctf.sandbox.js`
10. `overviewCache.js`

These define:
- security
- business rules
- platform lifecycle
- token economy
- performance behavior
- student progression

---

# Recommended Future Improvements

## Infrastructure
- Redis caching
- queue workers
- websocket notifications
- distributed job processing
- observability dashboards

---

## Security
- audit logging
- session anomaly detection
- IP reputation scoring
- encrypted sensitive fields
- zero-trust internal APIs

---

## Developer Experience
- OpenAPI/Swagger docs
- centralized schema validation
- typed API contracts
- integration test expansion

---

# Final Notes

The backend architecture already shows:
- modular thinking
- domain separation
- scalability awareness
- security consciousness

That puts it ahead of a disturbing percentage of production systems currently held together by:
```js
// temporary fix
```

written in 2021 and feared by everyone ever since.
